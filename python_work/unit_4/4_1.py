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
#��ֵ�bug�����ˣ�ԭ���������˵ڶ���print�й���
squares=[]
for value in range(1,11):
	squares.append(value**2)
print(squares)

#ר�Ŵ������ֵĺ���
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

#���������б����б����
#�����б�
print('\n')
squares=[]
for value in range(1,11):
	square=value**2
	squares.append(square)
print(squares)

#�����������б�
print('\n')
squares=[]
for value in range(1,11):
	squares.append(value**2)
print(squares)

#�����б�
print('\n')
squares=[value**2 for value in range(1,11)]
print(squares)

#4-4 ��Ƭ
players = ['charles', 'martina', 'michael', 'florence', 'eli']

#ָ����������Ҫע�����ֺ�ʵ��˳��֮�����һλ
print(players[0:3]) 
print(players[1:4])

#û��ָ����ʼ�������Զ����б�ͷ
print(players[:4])

#û��ָ�������������Զ���ֹ���б�ĩβ
print(players[2:])

#�������������б������λ��Ա
print(players[-3:])

print('\n')
for player in players[:3]:
	print(player.title())
