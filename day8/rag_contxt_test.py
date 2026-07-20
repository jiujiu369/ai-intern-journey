"""
Day8 上下文对照实验
核心原理：大模型回答完全依赖输入上下文
这是RAG解决幻觉、私有知识问答的底层逻辑
"""
from openai import OpenAI

client = OpenAI(
    api_key="sk-9346ceae7e4e4945a26668b8f5fa4d4b",
    base_url="https://api.deepseek.com/v1",
)
MODEL_NAME = "deepseek-v4-pro"

def llm_answer(question: str, context: str) -> str:
    """
    传入上下文，让模型基于上下文回答
    """
    prompt = f"""
请严格依据下方【参考背景】回答问题，背景无相关信息则回答“不知道”。
【参考背景】：{context}
【用户问题】：{question}
    """
    res = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return res.choices[0].message.content


if __name__ == "__main__":
    # 业务问题（私有知识，模型训练数据没有）
    query = input("请输入问题：")
    true_context = input("请输入正确的上下文：")
    wrong_context = input("请输入错误的上下文：")
    # 场景1：无上下文
    print("========== 1. 无任何上下文 ==========")
    contxt = ""
    print(llm_answer(query, context=""))

    # 场景2：正确业务上下文
    print("\n========== 2. 携带正确业务上下文 ==========")
    
    print(llm_answer(query, true_context))

    # 场景3：错误上下文（验证模型跟随性）
    print("\n========== 3. 携带错误上下文 ==========")

    print(llm_answer(query, wrong_context))