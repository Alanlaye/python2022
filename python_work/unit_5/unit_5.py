#coding=utf-8
#5.2.1 检查是否相等 ==
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw': 
        print(car.upper())
    else:
        print(car.title())
        
#5.2.2 检查是否相等时不考虑大小写 if car.lower() == 'audi'
print('\n')
cars = ['Audi', 'bmw', 'subaru', 'toyota']
for car in cars:
	if car.lower() == 'audi':
		print(car.upper())
	else:
		print(car.title())
		

#5.2.3 检查是否不相等 ！=
print('\n')
requested_topping = 'mushrooms'
if requested_topping != 'anchovies': 
    print("Hold the anchovies!")

#5.2.4 比较数字
answer = 17
if answer != 42: 
    print("That is not the correct answer. Please try again!")
    
age = 19
if age < 21:
	print('True')


#5.2.5 检查多个条件 and or
#and
print('\n')
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21
###有一个问题，类似判断大小等可以直接在python里判断的怎么写在文本编辑器里呢？
#为了改善可读性，可以将每个测试放在一对括号中
(age_0 >= 21) and (age_1 >=21)

#or
age_1 = 22
age_1 = 18
age_0 >= 21 or age_1 >=21
(age_0 >= 21) or (age_1 >=21)

#5.2.6 检查特定值是否包含在列表中 in
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings 

#5.2.7 检查特定值是否不包含在列表中
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users: 
    print(user.title()+", you can post a response if you wish.")

#那么如果我按照之前那种判定式写呢？——答案是也可以
banned_users = ['andrew', 'carolina', 'david']
'marie' not in banned_users
'andrew' in banned_users

#5.2.8 布尔表达式
game_active = True
can_edit = False

print('\n')


#5-3 if语句
#5.3.1 if-do语句
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

#5.3.2 if-else语句
print('\n')
age = 17
if age >= 18: 
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else: 
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

#5.3.3 if-elif-else结构
print('\n')
age = 12
if age < 4:
	print("Your admission cost is $0.")
elif age < 18:
	 print("Your admission cost is $5.")
else:
	 print("Your admission cost is $10.")
#更简洁的表述
print('\n')
age = 12
if age < 4:
	price = 0
elif age < 18:
	price = 5
else:
	price = 10
print("Your admission cost is $"+str(price)+".")

#5.3.4 使用多个elif代码块
#场景：假设对于65岁（含）以上的老人，可以半价（即5美元）购买门票
print('\n')
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65: 
    price = 10
else: 
    price = 5
print("Your admission cost is $"+str(price)+".")

#5.3.5 省略else代码块
#else是一条包罗万象的语句，只要不满足任何if或elif中的条件测试
#其中的代码就会执行，这可能会引入无效甚至恶意的数据。
#如果知道最终要测试的条件，应考虑使用一个elif代码块来代替else代码块。
print('\n')
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65: 
    price = 5
print("Your admission cost is $"+str(price)+".")


#5.3.6 测试多个条件
#总之，如果你只想执行一个代码块，就使用if-elif-else结构；如果要运行多个代码块，就使用一系列独立的if语句。
#if-elif-else结构只通过一个测试；而系列独立的if语句则要求通过所有测试
print('\n')
requested_toppings = ['mushrooms', 'extra cheese'] 
if 'mushrooms' in requested_toppings: 
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings: 
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings: 
    print("Adding extra cheese.")
print("Finished making your pizza!")

#5.4 使用if语句处理列表
#5.4.1 检查特殊元素
#初始 简单for循环
print('\n')
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print("Adding "+requested_topping+".")
print("Finished making your pizza!")

#青椒用完了？
print('\n')
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print("Sorry!")
	else:
		print("Adding "+requested_topping+".")
print("Finished making your pizza!")

#总结：列表；for——if—else——print

#5.4.2 确定列表不是空的
print('\n')
requested_toppings = [] 
if requested_toppings: 
    for requested_topping in requested_toppings:
        print("Adding "+requested_topping+".")
    print("\nFinished making your pizza!")
else: 
    print("Are you sure you want a plain pizza?")
    
#试试再加上没青椒的情况？
print('\n')
requested_toppings = [] 
if requested_toppings: 
	for requested_topping in requested_toppings:
		if requested_topping == 'green peppers':
			print("Sorry!")
		else:
			print("Adding "+requested_topping+".")
	print("\nFinished making your pizza!")
else: 
	print("Are you sure you want a plain pizza?")
	
#5.4.3 使用多个列表
print('\n')
available_toppings = ['mushrooms', 'olives', 'green peppers', 
                      'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese'] 
for requested_topping in requested_toppings: 
    if requested_topping in available_toppings: 
        print("Adding "+requested_topping+".")
    else: 
        print("Sorry, we don't have "+requested_topping+".")
print("\nFinished making your pizza!")

