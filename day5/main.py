from utils import process_single_file, process_folder

if __name__ == "__main__":
    # 单文件测试
    print("===== 单文件测试 =====")
    text = process_single_file(r"F:\code\ai-intern-journey\day5\test\test1.docx")
    
    print(text)

    # 批量测试
    print("\n===== 文件夹测试 =====")
    batch = process_folder(r"F:\code\ai-intern-journey\day5\test")
    for item in batch:
        print(f"文件名：{item['name']} 清洗后长度：{len(item['clean_text'])}")