class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"我叫{self.name}，今年{self.age}岁"

s1 = Student("Alice", 20)
s2 = Student("Bob", 22)
print(s1.introduce())
print(s2.introduce())

class book :
	def __init__(self, title, author):
		self.title = title
		self.author = author	
	def introduce(self):
		return f"书名：{self.title}，作者：{self.author}"
s1 = book("Python编程", "张三")
s2 = book("数据结构", "李四")		
print(s1.introduce())
print(s2.introduce())


