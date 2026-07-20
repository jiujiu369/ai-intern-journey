def keyword_search(query: str, texts: list[str]) -> list[str]:
    """传统字面关键词检索"""
    res = []
    for text in texts:
        if query in text:
            res.append(text)
    return res

# 测试场景
if __name__ == "__main__":
    knowledge_texts = [
        "员工出差差旅费报销需提供发票、行程单、出差审批单，报销时限为出差结束后15个工作日内。"
    ]
    # 口语化提问，无精准关键词匹配
    test_query = "出差报账要几天内交"
    result = keyword_search(test_query, knowledge_texts)
    print("关键词检索结果：", result)  # 输出：[] 检索失败
