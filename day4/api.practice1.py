# 导入网络请求库
import requests

# 1. 接口地址（免费公开测试API，无需密钥）
url = "https://jsonplaceholder.typicode.com/posts/1"

# 2. 发送GET请求
response = requests.get(url)

# 3. 打印基础响应信息
print("HTTP状态码：", response.status_code)
print("-" * 50)

# 4. 解析JSON数据（核心步骤）
data = response.json()

# 5. 提取JSON中指定字段打印
print("文章ID：", data["id"])
print("文章标题：", data["title"])
print("文章内容：", data["body"])


# POST提交JSON数据示例
post_url = "https://jsonplaceholder.typicode.com/posts"

# 要传给服务器的JSON参数
send_data = {
    "title": "Day4 API练习",
    "body": "学习HTTP、JSON、requests调用接口",
    "userId": 10
}

# headers声明传输格式为json
headers = {
    "Content-Type": "application/json"
}

# 发送POST请求
res = requests.post(post_url, json=send_data, headers=headers)
result = res.json()
print("\n===== POST提交返回结果 =====")
print(result)