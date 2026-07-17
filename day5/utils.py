## 根据文件扩展名获取对应的解析器
import os
from document_parser import parse_txt_md, parse_pdf, parse_docx
from text_cleaner import full_text_clean
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

