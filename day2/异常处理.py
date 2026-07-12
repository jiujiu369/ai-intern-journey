while True:
    try:
        num = int(input("请输入数字："))
        print(num)
        break
    except ValueError:
        print("你输入的不是数字")

while True:
    try:
        with open("acs.txt", "r", encoding="utf-8") as f:
            print(f.read())
        break
    except FileNotFoundError:
        print("文件不存在")
    try:
        with open("test.txt", "r", encoding="utf-8") as f:
            print(f.read())
        break
    except FileNotFoundError:
        print("文件不存在")