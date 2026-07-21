
# 【完全可控版】RAG Prompt 模板
# 核心特性：自主控制文档、自主控制问题、严格防幻觉、强制溯源、精准拒答
# 适配课程Day9落地，可直接用于后续RAG项目
from openai import OpenAI
# 复用Day8 全局LLM配置（完全自主可控）
client = OpenAI(
    api_key="sk-9346ceae7e4e4945a26668b8f5fa4d4b",
    base_url="https://api.deepseek.com/v1",
)
MODEL_NAME = "deepseek-v4-pro"
# ====================== 1. 自主可控：内置知识库文档（自己掌控输入文档） ======================
# 所有RAG检索上下文由自己定义，杜绝不可控输入
DOC_KNOWLEDGE = [
    {
        "content": "员工出差差旅费报销时限为出差结束后15个工作日内，逾期不予受理。",
        "source": "公司报销管理制度V2.0.pdf"
    },
    {
        "content": "差旅费报销必须提交：出差审批单、交通票据、住宿发票，缺一不可。",
        "source": "公司报销管理制度V2.0.pdf"
    },
    {
        "content": "工作日上班时间为上午9:00-12:00，下午14:00-18:00，周末双休。",
        "source": "企业考勤管理制度.md"
    }
]
# ====================== 2. 自主可控：三类标准测试问题（全覆盖场景） ======================
TEST_QUERIES = {"请输入测试问题（可直接粘贴）：\n"
					 "1. 知识库有答案的标准问题\n"
					 "2. 知识库无答案的拒答问题\n"
					 "3. 知识库有答案，但问题与知识库不匹配的	误导问题\n"
					 "请输入问题编号（1/2/3）或直接输入自定义问题："
                    

				}
query1 = input("1. 知识库有答案的标准问题：\n")
# ====================== 3. 核心RAG Prompt（强约束、完全可控、防幻觉天花板） ======================
RAG_STATIC_PROMPT = """
你是企业内部知识库专属答疑助手，你的所有回答完全、只能、仅能基于给定参考文档。

【绝对硬性规则，违反即为错误回答】
1. 无文档内容 = 绝对禁止猜测、禁止补充常识、禁止拓展知识，必须固定拒答
2. 所有回答结论，必须精准对应参考文档原文
3. 每一条有效结论，必须尾部标注来源：[来源：xxx]
4. 回答简洁、精准、不闲聊、不冗余
5. 遇到超出知识库范围、无关、无法匹配的问题，只允许输出固定话术：
『抱歉，当前知识库中没有相关问题的解答，无法为您回答。』

【参考文档】
{context}

【用户问题】
{query}

【规范回答】
"""
# ====================== 4. 工具函数：自主组装上下文（可控文档格式） ======================
def build_rag_context(doc_list):
        """自主格式化文档，统一规范输入，避免格式混乱导致幻觉"""
        context_text = ""
        for idx, doc in enumerate(doc_list, 1):
            context_text += f"【文档{idx}】{doc['content']} [来源：{doc['source']}]\n"
        return context_text.strip()
# ====================== 5. 统一LLM调用（可控温度、可控参数） ======================
def rag_chat(query: str) -> str:
    # 自主组装文档上下文
    context = build_rag_context(DOC_KNOWLEDGE)
    # 自主拼接最终Prompt（完全自己掌控输入）
    prompt = RAG_STATIC_PROMPT.format(context=context, query=query)
    # 问答场景固定temperature=0，彻底抑制发散幻觉
    res = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0
    )
    return res.choices[0].message.content.strip()
# ====================== 6. 一键运行三类场景测试 ======================
if __name__ == "__main__":
    print("========== RAG 完全可控 Prompt 测试开始 ==========\n")
    for case_name, question in TEST_QUERIES.items():
        print(f"【测试场景：{case_name}】")
        print(f"用户问题：{question}")
        answer = rag_chat(question)
        print(f"模型回答：{answer}\n")
        print("-" * 80 + "\n")