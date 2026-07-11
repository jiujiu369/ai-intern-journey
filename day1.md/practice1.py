print("练习1：输入年龄、名字和学校名称，并打印一句话")
name = input("你好，请输入你的名字：").strip()
while not name:	
	print("名字不能为空，请重新输入。")
	name = input("你好，请输入你的名字：").strip()
	

school = input("请输入你的学校名称：").strip()
while not school:
	print("学校名称不能为空，请重新输入。")
	school = input("请输入你的学校名称：").strip()
	
while True:
	s = input("请输入你的年龄：(请输入整数)").strip()

	age = float(s)
	if age >= 0:
		break
	else:
			print("输入的年龄必须是正数，请重新输入。")
print(f"恭喜你，{school}的{name}，你今年{age}岁，完成练习")
