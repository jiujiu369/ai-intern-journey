import numpy as np

def cosine_similarity(vec1: list[float], vec2: list[float]) -> float:
    """
    手动实现余弦相似度公式
    返回值范围 [-1, 1]
    """
    v1 = np.array(vec1)
    v2 = np.array(vec2)

    dot = np.dot(v1, v2)
    norm1 = np.linalg.norm(v1)
    norm2 = np.linalg.norm(v2)

    score = dot / (norm1 * norm2)
    return float(score)