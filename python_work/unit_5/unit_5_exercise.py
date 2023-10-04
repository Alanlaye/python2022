#coding=utf-8
#5-2 条件测试
#不重要，一个参照列表
flowers = ['Calla','lily','carnation','daisy','Chrysanthemum','kalanchoe','iris']

#将'Calla'存储到变量flo中
flo = 'Calla'

#不重要，一个猜测的陈述
print("Is flo == 'Calla'? I predict True.")

#检查是否相等并输出结果（True or False）
print(flo == 'Calla')

#一些重复
flo = 'lily'
print("\nIs flo == 'lily'? I predict True.")
print(flo == 'lily')
flo = 'carnation'
print("\nIs flo == 'carnation'? I predict True.")
print(flo == 'carnation')
print("\nIs flo == 'lily'? I predict True.")
print(flo == 'lily')
flo = 'lily'
print("\nIs flo == 'lily'? I predict True.")
print(flo == 'lily')
#我懂了，取决于被赋予变量最新的值

#其他测试
#是否相等
print('\n')
cars = ['audi', 'bmw', 'subaru', 'toyota']
car = 'bmw'
print(car == 'bmw')

#是否不相等
print('\n')
requested_topping = 'mushrooms'
print(requested_topping != 'anchovies')

#比较数字和检查多个条件
print('\n')
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)
print(age_0 >= 21 or age_1 >= 21)

#检查是否被包含
print('\n')
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushroom' in requested_toppings)
print('mushroom' not in requested_toppings)


#5-3 if语句
print('\n')
alien_color = 'red'
if alien_color == 'green':
	print("Congradulations! You get 5 points!")

alien_color = 'green'
if alien_color == 'green':
	print("Congradulations! You get 5 points!")

print('\n')
alien_color = 'red'
if alien_color == 'green':
	print("Congradulations! You get 5 points!")
else:
	print("Congradulations! You get 10 points!")

print('\n')
alien_color = 'red'
if alien_color == 'green':
	print("Congradulations! You get 5 points!")
elif alien_color == 'yellow':
	print("Congradulations! You get 10 points!")
else:
	print("Congradulations! You get 15 points!")

alien_color = 'green'
if alien_color == 'green':
	print("Congradulations! You get 5 points!")
elif alien_color == 'yellow':
	print("Congradulations! You get 10 points!")
else:
	print("Congradulations! You get 15 points!")

alien_color = 'yellow'
if alien_color == 'green':
	print("Congradulations! You get 5 points!")
elif alien_color == 'yellow':
	print("Congradulations! You get 10 points!")
else:
	print("Congradulations! You get 15 points!")

print('\n')
age = 19
if age < 2:
	print('He is a baby.')
elif age < 4:
	print('He is a toddler.')
elif age < 13:
	print('He is a child.')
elif age < 20:
	print('He is a teenager.')
elif age < 65:
	print('He is an adult.')
else:
	print('He is an old man.')

print('\n')	
flowers=['Calla','lily','iris']
if 'Calla' in flowers:
	print("You really like Calla!")
if 'lily' in flowers:
	print("You really like lily!")
	

#5-4 if语句与列表处理
#以特殊方式跟管理员打招呼
print('\n')	
users = ['Calla','lily','carnation','daisy','kalanchoe','iris']
for user in users:
	if user == 'lily':
		print('Morning darling!'+'My dearest '+user+'!')
	else:
		print('Morning,'+user+'!')

#处理没有用户的情形
#这里的if users与之同级的else是什么意思 其实我没看都
#先不for循环，先对列表进行是否为空进行一个判定（？）
print('\n')	
users=[]
if users:
	for user in users:
		if user == 'lily':
			print('Morning darling!'+'My dearest '+user+'!')
		else:
			print('Morning,'+user+'!')
else:
	print('We need to find some users!')		
		
#检查用户名
print('\n')	
current_users = ['Calla','lily','carnation','daisy','kalanchoe','iris']
new_users = ['Chrysanthemum','rose','mili','daisy','kalanchoe']
for new_user in new_users:
	if new_user in current_users:
		print(new_user+' has been used!')
	else:
		print(new_user+' can be used!')
		
#不区分大小写检查用户名
#我草 写的什么垃圾 又臭又长 就一定要用这么复杂的变量命名吗
print('\n')	
current_users = ['Calla','lily','carnation','daisy','kalanchoe','iris']
new_users = ['Chrysanthemum','rose','mili','daisy','Kalanchoe']
#列表里的人名全部变成小写
current_users = ['Calla','lily','carnation','daisy','kalanchoe','iris']
current_users_lower = [current_user.lower() for current_user in current_users]
#很蠢，只需要做current_users一个列表的.lower就可以了，另外一个没必要
#判定重复与否部分
print('\n')	
for new_user in new_users:
	if new_user.lower() in current_users_lower:
		print(new_user+' has been used!')
	else:
		print(new_user+' can be used!')

#序数
#疑问是：== 表示两个字符相同，那么为什么第179行和182行出现的1是作为数字呢？
numbers = list(range(1,10))
print(numbers)
for number in numbers:
	if number == 1:
		print('1st')
	elif number == 2:
		print('2nd')
	elif number == 3:
		print('3rd')
	else:
		print(str(number)+'th')
#妈的 终于de出来了 所以我理解了 179 182行 当它们在==一侧就说明了它们已经被作为字符
#但是189行的number需要被变成字符
#而str()是个函数，不是方法......
 
#最后 格式：在诸如==、>=和<=等比较运算符两边各添加一个空格 





















