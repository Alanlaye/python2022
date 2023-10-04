#coding=utf-8
magicians = ['alice', 'david', 'carolina'] 
for magician in magicians: 
	print(magician) 

members=['Yaminy','Alan','Laye']
for member in members:
	print(member.title()+",welcome to my wedding!")
	print("I can't wait to see you,"+member.title()+"!")

three= list(range(3,15,3))
print(three)
print('\n')

squares=[]
for value in range(1,11):
	square=value**2
	squares.append(square)
print(squares)

#simplier
squares=[]
for value in range(1,11):
	squares.append(value**2)
	print(squares)
#奇怪的bug发生了，原来了缩进了第二个print行哈哈
squares=[]
for value in range(1,11):
	squares.append(value**2)
print(squares)

#专门处理数字的函数
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

#尝试生成列表与列表解析
#生成列表
print('\n')
squares=[]
for value in range(1,11):
	square=value**2
	squares.append(square)
print(squares)

#更简洁地生成列表
print('\n')
squares=[]
for value in range(1,11):
	squares.append(value**2)
print(squares)

#解析列表
print('\n')
squares=[value**2 for value in range(1,11)]
print(squares)

#4-4 切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']

#指定索引，需要注意数字和实际顺序之间差了一位
print(players[0:3]) 
print(players[1:4])

#没有指定开始索引，自动从列表开头
print(players[:4])

#没有指定结束索引，自动终止于列表末尾
print(players[2:])

#负数索引——列表最后三位成员
print(players[-3:])

print('\n')
for player in players[:3]:
	print(player.title())
