# day9/basic_prompt_test.py
from openai import OpenAI

# 复用Day8配置
client = OpenAI(
    api_key="sk-9346ceae7e4e4945a26668b8f5fa4d4b",
    base_url="https://api.deepseek.com/v1",
)
MODEL_NAME = "deepseek-v4-pro"

def chat(prompt: str, temperature: float = 0.0) -> str:
    """通用LLM调用函数，问答场景温度固定0抑制发散幻觉"""
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    # 测试素材
    query = "公司差旅费报销时限是多久？"
    context = "员工出差差旅费报销时限为出差结束后15个工作日内，逾期不予受理。[来源：报销制度.pdf]"
    print("===== 提示词对比实验开始 =====\n"
          "【实验素材】\n"
          f"问题：{query}\n"
          f"参考资料：{context}\n"
          )


    # 实验组1：无约束模糊提问（新手最容易写的写法）
    prompt1 = f"参考资料：{context}\n问题：{query}"
    res1 = chat(prompt1)
    print("【实验组1：无任何约束】")
    print(res1, "\n" + "-"*60 + "\n")

    # 实验组2：角色设定+基础指令约束（技巧1+技巧2）
    prompt2 = f"""你是公司行政知识库专属客服。
严格基于下方参考资料回答用户问题，禁止编造资料以外的内容。
参考资料：{context}
用户问题：{query}"""
    res2 = chat(prompt2)
    print("【实验组2：角色+明确指令约束】")
    print(res2, "\n" + "-"*60 + "\n")

    # 实验组3：角色+指令+输出格式+幻觉边界约束（全套RAG基础规则）
    prompt3 = f"""你是公司行政知识库专属客服。
# 强制规则
1. 回答100%仅使用参考资料内容，严禁补充外部知识、猜测、拓展
2. 回答末尾必须标注来源，格式固定：[来源：文档名]
3. 资料无对应内容直接回复：无法根据现有知识库解答该问题
参考资料：{context}
用户问题：{query}"""
    res3 = chat(prompt3)
    print("【实验组3：完整约束（角色+指令+格式+幻觉抑制）】")
    print(res3)