name = input("请输入你的名字：")
def add(a, b):
    return a + b
def bijiao(a, b):
	if a > b:
		return a
	else:
		return b
	
a = float(input("输入第一个数字："))
b = float(input("输入第二个数字："))
print(f"两个数之和是：{add(a, b)}")
print(f"更大的是：{bijiao(a,b)}")
print(f"欢迎你，{name}")


