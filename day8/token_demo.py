"""
Day8 Token 工程实战
功能：掌握Token计数、中英文比例、上下文窗口约束
核心价值：RAG分块、对话截断、成本预估、避免接口报错的底层依据
"""
from openai import OpenAI

# 初始化客户端（复用你之前的配置）
client = OpenAI(
    api_key="sk-9346ceae7e4e4945a26668b8f5fa4d4b",
    base_url="https://api.deepseek.com/v1",
)

def count_token_by_api(text: str, model: str = "deepseek-v4-pro") -> int:
    """
    通用Token统计方法：适配所有大模型
    :param text: 输入文本
    :param model: deepseek-v4-pro
    :return: 输入Token数量
    """
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": text}],
        max_tokens=1,  # 只统计输入，不生成内容，节省费用
        temperature=0
    )
    # 从接口返回值获取精准输入Token数
    return response.usage.prompt_tokens

if __name__ == "__main__":
    # 梯度测试：短、中、长文本
    while True:
        user_input = input("\n请输入测试文本（输入exit退出）：").strip()
        if user_input.lower() == "exit":
            break
        token_count = count_token_by_api(user_input)
        print(f"✅ 输入文本Token数量：{token_count}")

    print("\n【工程结论】中文1汉字 ≈ 1.3~1.5 Token，严禁按字数估算窗口！")