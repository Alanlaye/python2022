#coding=utf-8
#5.2.1 ����Ƿ���� ==
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw': 
        print(car.upper())
    else:
        print(car.title())
        
#5.2.2 ����Ƿ����ʱ�����Ǵ�Сд if car.lower() == 'audi'
print('\n')
cars = ['Audi', 'bmw', 'subaru', 'toyota']
for car in cars:
	if car.lower() == 'audi':
		print(car.upper())
	else:
		print(car.title())
		

#5.2.3 ����Ƿ���� ��=
print('\n')
requested_topping = 'mushrooms'
if requested_topping != 'anchovies': 
    print("Hold the anchovies!")

#5.2.4 �Ƚ�����
answer = 17
if answer != 42: 
    print("That is not the correct answer. Please try again!")
    
age = 19
if age < 21:
	print('True')


#5.2.5 ��������� and or
#and
print('\n')
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21
###��һ�����⣬�����жϴ�С�ȿ���ֱ����python���жϵ���ôд���ı��༭�����أ�
#Ϊ�˸��ƿɶ��ԣ����Խ�ÿ�����Է���һ��������
(age_0 >= 21) and (age_1 >=21)

#or
age_1 = 22
age_1 = 18
age_0 >= 21 or age_1 >=21
(age_0 >= 21) or (age_1 >=21)

#5.2.6 ����ض�ֵ�Ƿ�������б��� in
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings 

#5.2.7 ����ض�ֵ�Ƿ񲻰������б���
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users: 
    print(user.title()+", you can post a response if you wish.")

#��ô����Ұ���֮ǰ�����ж�ʽд�أ���������Ҳ����
banned_users = ['andrew', 'carolina', 'david']
'marie' not in banned_users
'andrew' in banned_users

#5.2.8 �������ʽ
game_active = True
can_edit = False

print('\n')


#5-3 if���
#5.3.1 if-do���
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

#5.3.2 if-else���
print('\n')
age = 17
if age >= 18: 
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else: 
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

#5.3.3 if-elif-else�ṹ
print('\n')
age = 12
if age < 4:
	print("Your admission cost is $0.")
elif age < 18:
	 print("Your admission cost is $5.")
else:
	 print("Your admission cost is $10.")
#�����ı���
print('\n')
age = 12
if age < 4:
	price = 0
elif age < 18:
	price = 5
else:
	price = 10
print("Your admission cost is $"+str(price)+".")

#5.3.4 ʹ�ö��elif�����
#�������������65�꣨�������ϵ����ˣ����԰�ۣ���5��Ԫ��������Ʊ
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

#5.3.5 ʡ��else�����
#else��һ�������������䣬ֻҪ�������κ�if��elif�е���������
#���еĴ���ͻ�ִ�У�����ܻ�������Ч������������ݡ�
#���֪������Ҫ���Ե�������Ӧ����ʹ��һ��elif�����������else����顣
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


#5.3.6 ���Զ������
#��֮�������ֻ��ִ��һ������飬��ʹ��if-elif-else�ṹ�����Ҫ���ж������飬��ʹ��һϵ�ж�����if��䡣
#if-elif-else�ṹֻͨ��һ�����ԣ���ϵ�ж�����if�����Ҫ��ͨ�����в���
print('\n')
requested_toppings = ['mushrooms', 'extra cheese'] 
if 'mushrooms' in requested_toppings: 
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings: 
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings: 
    print("Adding extra cheese.")
print("Finished making your pizza!")

#5.4 ʹ��if��䴦���б�
#5.4.1 �������Ԫ��
#��ʼ ��forѭ��
print('\n')
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print("Adding "+requested_topping+".")
print("Finished making your pizza!")

#�ཷ�����ˣ�
print('\n')
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print("Sorry!")
	else:
		print("Adding "+requested_topping+".")
print("Finished making your pizza!")

#�ܽ᣺�б�for����if��else����print

#5.4.2 ȷ���б��ǿյ�
print('\n')
requested_toppings = [] 
if requested_toppings: 
    for requested_topping in requested_toppings:
        print("Adding "+requested_topping+".")
    print("\nFinished making your pizza!")
else: 
    print("Are you sure you want a plain pizza?")
    
#�����ټ���û�ཷ�������
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
	
#5.4.3 ʹ�ö���б�
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

