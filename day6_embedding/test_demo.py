# 路径适配代码，解决同目录导入ModuleNotFoundError
import sys      
from pathlib import Path  
sys.path.insert(0, str(Path(__file__).resolve().parent)) 

# 导入本地向量化、相似度函数
from embedding_local import get_local_embedding
from cos import cosine_similarity

if __name__ == "__main__":
    # 手动自定义输入三句文本
    text_a = input("请输入参考句子（基准文本）：")
    text_b = input("请输入对比句子1（相近语义）：")
    text_c = input("请输入对比句子2（无关语义）")

    # 离线生成向量
    vec_a = get_local_embedding(text_a)
    vec_b = get_local_embedding(text_b)
    vec_c = get_local_embedding(text_c)

    # 计算相似度
    sim_ab = cosine_similarity(vec_a, vec_b)
    sim_ac = cosine_similarity(vec_a, vec_c)

    # 打印结果
    print("===== 本地离线Embedding语义相似度实验 =====")
    print(f"语义相近两句话相似度：{sim_ab:.4f}")
    print(f"语义无关两句话相似度：{sim_ac:.4f}")
    print("===========================================")