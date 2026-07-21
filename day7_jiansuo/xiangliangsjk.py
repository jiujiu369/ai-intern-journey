# 路径修复：让代码能找到day5、day6
import sys
from pathlib import Path
# 项目根目录加入搜索路径
root_path = str(Path(__file__).parent.parent)
sys.path.insert(0, root_path)

import os
import chromadb
from chromadb.api.types import Documents, EmbeddingFunction, Embeddings

# 导入Day6本地向量化
from day6_embedding.embedding_local import get_local_embedding
# 导入Day5文档处理全套工具
from day5.utils import process_single_file, process_folder, split_chunk

# ---------------------- 复用你interactive_test1.py的文件查找函数 ----------------------
def find_file_in_day5(user_input: str):
    """根据用户输入，自动查找文件：绝对路径 / day5内文件名"""
    day5_dir = Path(root_path) / "day5"
    # 1. 如果输入是完整存在路径，直接返回
    if os.path.exists(user_input):
        return user_input
    # 2. day5目录下拼接相对路径
    relative_candidate = os.path.join(day5_dir, user_input)
    if os.path.exists(relative_candidate):
        return relative_candidate
    # 3. 递归遍历day5所有子文件夹匹配文件名
    for root, _, files in os.walk(day5_dir):
        for file_name in files:
            if file_name == user_input:
                return os.path.join(root, file_name)
    return None

# ---------------------- 原有向量库嵌入类不变 ----------------------
class LocalBGEEmbedding(EmbeddingFunction):
    def __call__(self, texts: Documents) -> Embeddings:
        return [get_local_embedding(text) for text in texts]

# ---------------------- 向量库工具类不变 ----------------------
class VectorDB:
    def __init__(self, persist_dir="./chroma_db", collection_name="knowledge_base"):
        self.client = chromadb.PersistentClient(path=persist_dir)
        self.embedding_fn = LocalBGEEmbedding()
        self.collection = self.client.get_or_create_collection(
            name=collection_name,
            embedding_function=self.embedding_fn,
            metadata={"hnsw:space": "cosine"}
        )

    def clear_collection(self):
        self.client.delete_collection(self.collection.name)
        self.collection = self.client.get_or_create_collection(
            name=self.collection.name,
            embedding_function=self.embedding_fn,
            metadata={"hnsw:space": "cosine"}
        )

    def add_documents(self, texts: list[str], metadatas: list[dict]):
        ids = [f"doc_{i}" for i in range(len(texts))]
        self.collection.add(documents=texts, metadatas=metadatas, ids=ids)

    def search(self, query_text: str, top_k: int = 3) -> list[dict]:
        res = self.collection.query(query_texts=[query_text], n_results=top_k)
        output = []
        for doc, meta, dist in zip(res["documents"][0], res["metadatas"][0], res["distances"][0]):
            output.append({
                "text": doc,
                "score": 1 - dist,
                "metadata": meta
            })
        return output

# ---------------------- 交互主程序（融合文件查找逻辑） ----------------------
if __name__ == "__main__":
    db = VectorDB()
    db.clear_collection()  # 首次测试取消注释清空旧库

    print("===== 离线RAG向量入库工具（支持文件名/完整路径输入）=====")
    default_file = r"F:\code\ai-intern-journey\day5\test\test1.docx"
    user_input = input(f"默认文档：{default_file}\n直接输入文件名/完整路径，回车使用默认文件：").strip()

    # 处理文件路径
    if not user_input:
        file_path = default_file
    else:
        file_path = find_file_in_day5(user_input)

    # 文件校验
    if not file_path or not os.path.exists(file_path):
        print(f"❌ 未找到文件：{user_input}")
        sys.exit()
    print(f"\n✅ 待处理文件：{file_path}")

    # 1.Day5全套解析+清洗
    clean_full_text = process_single_file(file_path)
    if clean_full_text == "文件不存在" or len(clean_full_text.strip()) == 0:
        print("❌ 文件无有效文本，终止入库")
        sys.exit()
    print(f"✅ 清洗完成，总字符数：{len(clean_full_text)}")

    # 2.文本滑动分块
    chunk_list = split_chunk(clean_full_text, chunk_size=300, overlap=60)
    print(f"✅ 文本分块完成，共 {len(chunk_list)} 个片段")

    # 3.构造元数据（记录来源文件名）
    file_name = Path(file_path).name
    meta_list = []
    for idx, seg in enumerate(chunk_list):
        meta_list.append({
            "source_file": file_name,
            "chunk_id": idx
        })

    # 4.批量离线向量化入库
    db.add_documents(chunk_list, meta_list)
    print("✅ 全部片段已存入本地向量库，持久化完成！")

    # 5.交互式语义检索循环
    print("\n===== 语义检索交互（输入exit退出） =====")
    while True:
        question = input("请输入你的问题：").strip()
        if question.lower() == "exit":
            print("程序结束")
            break
        result = db.search(question, top_k=2)
        print("\n---------- 检索结果 ----------")
        for i, item in enumerate(result):
            print(f"\nTop{i+1} 相似度分数：{item['score']:.4f}")
            print(f"来源文档：{item['metadata']['source_file']}")
            print(f"文本片段：{item['text']}")