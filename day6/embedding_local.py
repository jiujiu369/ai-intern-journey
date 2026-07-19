from sentence_transformers import SentenceTransformer

# 加载轻量中文向量模型，首次运行自动下载到本地，断网也能用
model = SentenceTransformer("BAAI/bge-base-zh-v1.5")

def get_local_embedding(text: str) -> list[float]:
    """
    本地离线生成文本向量，无需任何API、网络、密钥
    """
    text = text.replace("\n", " ").strip()
    vec = model.encode(text)
    return vec.tolist()


