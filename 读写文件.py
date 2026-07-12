# 写入文件
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("hello   world   nihao   ")

# 读取文件
with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()
print(content)  

#读取json文件
import json

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(data)

import json

data = {"name": "Tom", "age": 18}

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# 读取csv文件
import csv

with open("data.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

