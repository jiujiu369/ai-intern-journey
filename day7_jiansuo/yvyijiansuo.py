import sys
from pathlib import Path
# parent.parent 代表【项目根目录】，才能识别day6、day5文件夹
root_path = str(Path(__file__).parent.parent)
sys.path.insert(0, root_path)

import chromadb
from chromadb.api.types import Documents, EmbeddingFunction, Embeddings
from day6_embedding.embedding_local import get_local_embedding
from day5.utils import process_single_file, split_chunk


# 1. 自定义本地嵌入层（连接BGE模型与Chroma）
class LocalBGEEmbedding(EmbeddingFunction):
    def __call__(self, texts: Documents) -> Embeddings:
        return [get_local_embedding(text) for text in texts]

# 2. 向量库封装（包含完整语义检索核心search方法）
class VectorDB:
    def __init__(self, persist_dir="./test_chroma"):
        self.client = chromadb.PersistentClient(path=persist_dir)
        self.emb_fn = LocalBGEEmbedding()
        self.collection = self.client.get_or_create_collection(
            name="test_kb",
            embedding_function=self.emb_fn,
            metadata={"hnsw:space": "cosine"}
        )

    # 新增：清空向量库方法
    def clear_collection(self):
        self.client.delete_collection(self.collection.name)
        self.collection = self.client.get_or_create_collection(
            name="test_kb",
            embedding_function=self.emb_fn,
            metadata={"hnsw:space": "cosine"}
        )

    def add_text(self, text_list, meta_list):
        ids = [f"doc_{i}" for i in range(len(text_list))]
        self.collection.add(documents=text_list, metadatas=meta_list, ids=ids)

    # 语义检索核心函数
    def semantic_search(self, query: str, top_k=2):
        res = self.collection.query(query_texts=[query], n_results=top_k)
        output = []
        for doc, meta, dist in zip(res["documents"][0], res["metadatas"][0], res["distances"][0]):
            output.append({
                "text": doc,
                "similarity": 1 - dist,
                "meta": meta
            })
        return output

# 3. 交互入口
if __name__ == "__main__":
    db = VectorDB()
    db.clear_collection()  # 启动清空旧数据，避免新旧文档冲突

    # 文档解析：读取pdf/md/docx/txt
    file_path = input("输入文档完整路径：").strip()
    clean_text = process_single_file(file_path)
    if clean_text == "文件不存在" or len(clean_text.strip()) == 0:
        print("文件读取失败或无有效文本！")
        sys.exit()

    # 文本分块 + 生成元数据meta_list
    chunks = split_chunk(clean_text)
    file_name = Path(file_path).name
    meta_list = []
    for idx, seg in enumerate(chunks):
        meta_list.append({
            "source_file": file_name,
            "chunk_id": idx
        })

    # 批量入库（修正方法名）
    db.add_text(chunks, meta_list)
    print(f"✅ 文档{file_name}入库完成，共{len(chunks)}个文本片段")

    print("\n离线语义检索测试，输入exit退出\n")
    while True:
        q = input("你的问题：").strip()
        if q.lower() == "exit":
            print("程序结束")
            break
        search_res = db.semantic_search(q)
        for i, item in enumerate(search_res):
            print(f"\nTop{i+1} 相似度：{item['similarity']:.4f}")
            print(f"来源文档：{item['meta']['source_file']}")
            print(f"内容：{item['text']}")