## 根据文件扩展名获取对应的解析器
import os
from .document_parser import parse_txt_md, parse_pdf, parse_docx
from .text_cleaner import full_text_clean
def get_parser(file_path: str):
    suffix = file_path.split(".")[-1].lower()
    if suffix in ["txt", "md"]:
        return parse_txt_md
    elif suffix == "pdf":
        return parse_pdf
    elif suffix == "docx":
        return parse_docx
    else:
        raise Exception("不支持此文件格式")
    
## 单文件处理
def process_single_file(file_path: str) -> str:
    if not os.path.exists(file_path):
        return "文件不存在"
    parser = get_parser(file_path)
    raw = parser(file_path)
    clean = full_text_clean(raw)
    return clean

## 批量文件夹处理
def process_folder(folder_path: str) -> list:
    res = []
    support = ["txt","md","pdf","docx"]
    for root, _, files in os.walk(folder_path):
        for f in files:
            if f.split(".")[-1].lower() in support:
                path = os.path.join(root, f)
                res.append({
                    "name": f,
                    "clean_text": process_single_file(path)
                })
    return res


## 清洗后的长文本切分片段，用于向量入库（day7）
def split_chunk(text: str, chunk_size=300, overlap=60) -> list[str]:
    """
    清洗后的长文本切分片段，用于向量入库
    :param text: full_text_clean 清洗完成的全文
    :param chunk_size: 单块最大字符
    :param overlap: 块重叠字符，防止上下文断裂
    :return: 文本片段列表
    """
    chunks = []
    start = 0
    total_len = len(text)
    while start < total_len:
        end = start + chunk_size
        seg = text[start:end].strip()
        if seg:
            chunks.append(seg)
        start += chunk_size - overlap
    return chunks