## 1.清理不可见乱码控制字符
import re
def clean_control_char(text: str) -> str:
    return re.sub(r"[\x00-\x1F\x7F-\x9F]", "", text) ## 删除ASCII控制字符（0-31、127）和C1控制字符（128-159）

## 2.规整空白字符
def clean_blank_char(text: str) -> str:
    text = re.sub(r"\t+", " ", text)
    text = re.sub(r" +", " ", text)
    return text

## 3.删除连续空行
def clean_empty_line(text: str) -> str:
    lines = [line.strip() for line in text.split("\n")]
    valid = [line for line in lines if line]
    return "\n".join(valid)

## 4.过滤页码、页眉、版权重复文本
def clean_invalid_content(text: str) -> str:
    text = re.sub(r"第\d+页|Page \d+|版权所有.*|©.*", "", text)
    return text

## 5.清理无意义装饰符号
def clean_special_symbol(text: str) -> str:
    return re.sub(r"[#$%^&*_+=|~{}[\]]", "", text)

## 6.段落统一规整
def format_text(text: str) -> str:
    text = text.replace("\n\n", "\n")
    return text.strip()

# 一站式完整清洗流水线，按顺序执行全部6步清洗
def full_text_clean(text: str) -> str:
    if not text:
        return ""
    text = clean_control_char(text)
    text = clean_blank_char(text)
    text = clean_empty_line(text)
    text = clean_invalid_content(text)
    text = clean_special_symbol(text)
    text = format_text(text)
    return text