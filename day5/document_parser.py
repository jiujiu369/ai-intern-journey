## txt、markdown 解析
def parse_txt_md(file_path: str) -> str:
    try:
        # 优先utf-8打开，开发、Linux、记事本新建文件大多是utf8
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
    except UnicodeDecodeError:
        # Windows系统导出、老文档默认GBK，编码报错自动降级兼容
        with open(file_path, "r", encoding="gbk") as f:
            text = f.read()
    return text.strip()## 删除首尾空格

### PDF 解析
from PyPDF2 import PdfReader
def parse_pdf(file_path: str) -> str:
    text_list = []
    try:
        reader = PdfReader(file_path)
        # 遍历所有页面对象
        for page in reader.pages:
            page_text = page.extract_text()
            # 空白页面跳过，避免存入空字符串
            if page_text:
                text_list.append(page_text)
        # 所有页面文本用换行拼接，还原分页结构
        return "\n".join(text_list)
    except Exception as e:
        return f"PDF解析失败：{str(e)}"

## Word 解析  
from docx import Document
def parse_docx(file_path: str) -> str:
    text_list = []
    try:
        doc = Document(file_path)
        # 遍历文档全部段落对象，标题、正文都属于paragraphs
        for para in doc.paragraphs:
            t = para.text.strip()
            # 过滤空白段落，避免大量空行
            if t:
                text_list.append(t)
        return "\n".join(text_list)
    except Exception as e:
        return f"Word解析失败：{str(e)}"
