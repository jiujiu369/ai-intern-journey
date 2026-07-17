import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from utils import process_single_file


def find_file_in_day5(user_input: str):
    day5_dir = Path(__file__).resolve().parent

    # 1. 先看输入本身是不是已经是存在的路径
    if os.path.exists(user_input):
        return user_input

    # 2. 再看是不是 day5 目录下的相对路径
    relative_candidate = os.path.join(day5_dir, user_input)
    if os.path.exists(relative_candidate):
        return relative_candidate

    # 3. 在 day5 目录及子目录中递归查找文件名
    for root, _, files in os.walk(day5_dir):
        for file_name in files:
            if file_name == user_input:
                return os.path.join(root, file_name)

    return None


def main():
    print("===== 交互式单文件测试 =====")
    print("请输入文件名或者文件路径，或者直接回车使用默认文件")

    default_file = r"F:\code\ai-intern-journey\day5\test\test1.docx"
    user_input = input(f"默认文件：{default_file}\n请输入：").strip()

    if not user_input:
        file_path = default_file
    else:
        file_path = find_file_in_day5(user_input)

    if not file_path or not os.path.exists(file_path):
        print("没有找到这个文件：")
        print(user_input)
        return

    print(f"\n正在解析：{file_path}")
    text = process_single_file(file_path)
    print(text[:1200])


if __name__ == "__main__":
    main()