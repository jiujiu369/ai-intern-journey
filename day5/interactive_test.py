import os
import sys
from pathlib import Path

# 可以根据输入文件的地址，解析文件
sys.path.insert(0, str(Path(__file__).resolve().parent))

from utils import process_single_file


def main():
    print("===== 交互式单文件测试 =====")
    print("请输入要测试的文件路径，或者直接回车使用默认文件")

    default_file = r"F:\code\ai-intern-journey\day5\test\test1.docx"
    user_input = input(f"默认文件：{default_file}\n请输入：").strip()

    if not user_input:
        file_path = default_file
    else:
        file_path = user_input

    if not os.path.exists(file_path):
        print("文件不存在：")
        print(file_path)
        return

    print(f"\n正在解析：{file_path}")
    text = process_single_file(file_path)
    print(text)


if __name__ == "__main__":
    main()
