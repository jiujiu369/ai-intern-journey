import json

with open("faq.json", "w", encoding="utf-8") as f:
    json.dump({
        "什么是Python": "Python是一种编程语言。",
        "Python好学吗": "Python相对容易学习。",
        "什么是RAG": "检索增强生成，先检索本地知识库，再把参考资料交给大模型生成回答，缓解幻觉问题",
        "embedding是什么": "文本嵌入，将文字转化为低维数字向量，用来计算两段文字的语义相似度，是向量检索的基础",
        "Python虚拟环境作用": "隔离不同项目的第三方依赖包，防止不同项目库版本冲突",
        "LangChain是干嘛的": "大模型应用开发框架，封装RAG、Agent、工具调用等通用流程，快速搭建LLM程序"
    }, f)

def load_faq(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("FAQ 文件不存在")
        return {}

def ask_question(faq, question):
    return faq.get(question, "没找到这个问题的答案")

faq = load_faq("faq.json")

while True:
    q = input("请输入问题（输入 “退出” 退出）：")
    if q == "退出":
        break
    print(ask_question(faq, q))
