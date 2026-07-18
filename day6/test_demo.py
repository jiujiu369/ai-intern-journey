# 新增：路径适配代码，放在所有import最前面
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))

# 下面保持你原来的导入不变
from embedding_local import get_local_embedding
from cos import cosine_similarity

if __name__ == "__main__":
    # 你的测试代码不变
    #text_a = "公司报销差旅费需要准备哪些材料？"
    #text_b = "出差报销要提交什么单据和资料？"
    #text_c = "公司每周三下午提供免费下午茶和水果。"
    text_a = input("请输入参考句子（基准文本）：")
    text_b = input("请输入对比句子1（相近语义）：")
    text_c = input("请输入对比句子2（无关语义）：")

    vec_a = get_local_embedding(text_a)
    vec_b = get_local_embedding(text_b)
    vec_c = get_local_embedding(text_c)

    sim_ab = cosine_similarity(vec_a, vec_b)
    sim_ac = cosine_similarity(vec_a, vec_c)

    print("===== 本地离线Embedding语义相似度实验 =====")
    print(f"语义相近两句话相似度：{sim_ab:.4f}")
    print(f"语义无关两句话相似度：{sim_ac:.4f}")