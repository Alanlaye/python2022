#coding=utf-8
#5-2 ��������
#����Ҫ��һ�������б�
flowers = ['Calla','lily','carnation','daisy','Chrysanthemum','kalanchoe','iris']

#��'Calla'�洢������flo��
flo = 'Calla'

#����Ҫ��һ���²�ĳ���
print("Is flo == 'Calla'? I predict True.")

#����Ƿ���Ȳ���������True or False��
print(flo == 'Calla')

#һЩ�ظ�
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
#�Ҷ��ˣ�ȡ���ڱ�����������µ�ֵ

#��������
#�Ƿ����
print('\n')
cars = ['audi', 'bmw', 'subaru', 'toyota']
car = 'bmw'
print(car == 'bmw')

#�Ƿ����
print('\n')
requested_topping = 'mushrooms'
print(requested_topping != 'anchovies')

#�Ƚ����ֺͼ��������
print('\n')
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)
print(age_0 >= 21 or age_1 >= 21)

#����Ƿ񱻰���
print('\n')
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushroom' in requested_toppings)
print('mushroom' not in requested_toppings)


#5-3 if���
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
	

#5-4 if������б���
#�����ⷽʽ������Ա���к�
print('\n')	
users = ['Calla','lily','carnation','daisy','kalanchoe','iris']
for user in users:
	if user == 'lily':
		print('Morning darling!'+'My dearest '+user+'!')
	else:
		print('Morning,'+user+'!')

#����û���û�������
#�����if users��֮ͬ����else��ʲô��˼ ��ʵ��û����
#�Ȳ�forѭ�����ȶ��б�����Ƿ�Ϊ�ս���һ���ж�������
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
		
#����û���
print('\n')	
current_users = ['Calla','lily','carnation','daisy','kalanchoe','iris']
new_users = ['Chrysanthemum','rose','mili','daisy','kalanchoe']
for new_user in new_users:
	if new_user in current_users:
		print(new_user+' has been used!')
	else:
		print(new_user+' can be used!')
		
#�����ִ�Сд����û���
#�Ҳ� д��ʲô���� �ֳ��ֳ� ��һ��Ҫ����ô���ӵı���������
print('\n')	
current_users = ['Calla','lily','carnation','daisy','kalanchoe','iris']
new_users = ['Chrysanthemum','rose','mili','daisy','Kalanchoe']
#�б��������ȫ�����Сд
current_users = ['Calla','lily','carnation','daisy','kalanchoe','iris']
current_users_lower = [current_user.lower() for current_user in current_users]
#�ܴ���ֻ��Ҫ��current_usersһ���б��.lower�Ϳ����ˣ�����һ��û��Ҫ
#�ж��ظ���񲿷�
print('\n')	
for new_user in new_users:
	if new_user.lower() in current_users_lower:
		print(new_user+' has been used!')
	else:
		print(new_user+' can be used!')

#����
#�����ǣ�== ��ʾ�����ַ���ͬ����ôΪʲô��179�к�182�г��ֵ�1����Ϊ�����أ�
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
#��� ����de������ ����������� 179 182�� ��������==һ���˵���������Ѿ�����Ϊ�ַ�
#����189�е�number��Ҫ������ַ�
#��str()�Ǹ����������Ƿ���......
 
#��� ��ʽ��������==��>=��<=�ȱȽ���������߸����һ���ո� 





















