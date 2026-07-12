# 简易AI知识库
qa_dict = {
    "什么是RAG": "检索增强生成，先检索本地知识库，再把参考资料交给大模型生成回答，缓解幻觉问题",
    "embedding是什么": "文本嵌入，将文字转化为低维数字向量，用来计算两段文字的语义相似度，是向量检索的基础",
    "Python虚拟环境作用": "隔离不同项目的第三方依赖包，防止不同项目库版本冲突",
    "LangChain是干嘛的": "大模型应用开发框架，封装RAG、Agent、工具调用等通用流程，快速搭建LLM程序"
}

print("====简易问答机器人，输入exit退出====")
while True:
    try:
        question = input("你的问题：").strip()
        if question.lower() == "exit":
            print("程序退出！")
            break
        # 匹配知识库
        if question in qa_dict:
            print(f"回答：{qa_dict[question]}\n")
        else:
            print("回答：暂时没有收录这个问题，无法解答\n")
    except Exception as e:
        print(f"程序异常：{e}，请重新输入\n")