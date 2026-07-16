- 1.Linux核心命令
- pwd		显示当前路径
- ls		列出当前路径目录文件
- cd		切换文件夹
- mkdir		创建文件夹
- cat		读取完整文件内容
- grep		文件关键词检索
- rm		删除文件 / 文件夹

- 2.HTTP 协议 + JSON 规范 + API 原理 + Python requests 实操
- HTTP 协议基础
	(1)HTTP（超文本传输协议）是：**客户端 ↔ 服务器**之间传递数据的标准规则，浏览器 / 代码脚本是客户端，后端服务是服务器。
	(2)请求方式：GET/POST
		GET:从服务器获取数，无修改、无新增
		POST:向服务器提交数，新增 / 修改资源
	（3）HTTP 请求四要素（写 API 代码必带）
			请求地址 URL：接口网址，例如 `https://jsonplaceholder.typicode.com/posts`（免费、公开、永久可用的模拟测试 API 接口）
			请求方式：GET / POST
			请求体 Headers：携带身份、数据格式（常见 `Content-Type: application/json`）
			请求体 Body：POST 专用，传给服务器的 JSON 参数
- JSON 格式规范（API 数据通用格式）
	JSON 是轻量文本格式，前后端 / 接口统一交换数据，规则严格：
		键名必须用**双引号** `"key"`，不能单引号
		数据类型：字符串、数字、布尔、数组`[]`、对象`{}`、null
		键值对逗号分隔，最后一项**不能加逗号**
- 实操
1. 创建 API 练习文件
2. 使用免费的api接口测试接收和提交