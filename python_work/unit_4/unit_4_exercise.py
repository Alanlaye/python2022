#coding=utf-8
#换行 首字母大写
#4-1
flowers=['Calla','lily','daisy','iris']
for flower in flowers:
	print('\n'+'I like '+flower.title()+'.')
print('\n'+'I really love flowers!')

#4-2 for循环尝试
flowers=['Calla','lily','daisy','iris']
print('\n')
for flower in flowers:
	print(flower)

for flower in flowers:	
	print('\n')
	print(flower.title()+' is beautiful flower.')
print('\n')
print('Any of these animals would make a great pet!')

#4-3
print('\n')
for number in range(1,20):
	print(number)

#4-4
print('\n')
numbers=list(range(1,10))
print(numbers)
#试试更简洁的不创建新变量numbers）
print(list(range(1,10)))
#好耶成功！但是需要注意有三个括号

#4-5
print('\n')
numbers=list(range(1,101))
print(numbers)
print(min(numbers))
print(max(numbers))
print(sum(numbers))
#真的好容易忘记括号

#4-6  通过给函数range()指定第三个参数来创建一个列表，其中包含1～20的奇数；再使用一个for循环将这些数字都打印出来。
print('\n')
odd_numbers=list(range(1,20,2))
print(odd_numbers)
for odd_number in odd_numbers:
	print(odd_number)

#4-7
print('\n')
threes=list(range(3,30,3))
print(threes)
for three in threes:
	print(three)
	
#4-8 立方
#最朴实的描述
print('\n')
cubes=[]
for value in range(1,11):
	cube=value**3
	cubes.append(cube)
print(cubes)

#稍微简洁了一点
cubes=[]
for value in range(1,11):
	cubes.append(value**3)
print(cubes)

#4-9 最简洁 立方解析
cubes=[value**3 for value in range(1,11)]
print(cubes)

#4-10 cut
print('\n')
flowers=['Calla','lily','carnation','daisy','Chrysanthemum','kalanchoe','iris']
print('The first three items in the list are:')
print(flowers[:3])

print('\n')
print('Three items from the middle of the list are:')
n=int(len(flowers)/2)
for flower in flowers[n-1:n+2]:
   print(flower.title())

print('\n')
print('The last three items in the list are:')
print(flowers[-3:])

#4-11 
flowers=['Calla','lily','carnation','daisy','Chrysanthemum','kalanchoe','iris']
fr_flowers=flowers[:]
flowers.append('rose')
fr_flowers.append('muguet')
print(flowers)
print(fr_flowers)

print('My flowers are:')
for flower in flowers:
	print(flower)

print("My friend's flowers sre:")
for fr_flower in fr_flowers:
	print(fr_flower)

#4-13
flowers=('Calla','daisy','Chrysanthemum','kalanchoe','iris')
for flower in flowers:
	print(flower.title())

flowers=('lily','carnation','Calla','daisy','Chrysanthemum')
for flower in flowers:
	print(flower.title())
	
