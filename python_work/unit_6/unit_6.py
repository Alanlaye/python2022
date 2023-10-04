#coding=utf-8
#6.2 �ֵ�
alien_0 = {'color':'green','point':5}
print(alien_0['color'])
#ֱ��
print('You just earned '+str(alien_0['point'])+' points!')
#ͨ���������ʹ��Key-value
new_points = alien_0['point']
print('You just earned '+str(new_points)+' points!')
#����key-value
alien_0['x'] = 0
alien_0['y'] = 25
print(alien_0)
#�ӿ��ֵ俪ʼ�����ֵ�
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
#�޸���ֵ
alien_0['color'] = 'yellow'
print(alien_0)

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: "+str(alien_0['x_position']))
# �����ƶ�������
# �������˵�ǰ�ٶȾ��������ƶ���Զ
if alien_0['speed'] == 'slow': 
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # ��������˵��ٶ�һ���ܿ�
    x_increment = 3
# ��λ�õ�����λ�ü�������
alien_0['x_position'] = alien_0['x_position']+x_increment 
print("New x-position: "+str(alien_0['x_position']))

#ɾ��key-value del��䣨����ɾ����
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(alien_0)
del alien_0['speed']
print(alien_0)

###�����ƶ�����ɵ��ֵ䣨��ʽ��
f_ls = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print("Sarah's favorite language is "+	
	f_ls['sarah'].title()+
	'.')
#��ʾ����ν�print�д���ֳɼ���

#6.3 �����ֵ� 
# for key,value in user_0.items()
###��������key-value��
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }
for key,value in user_0.items():
	print('\nKey:'+key)
	print('Value:'+value)

for k,v in user_0.items():
	print('\nKey:'+k+';Value:'+v)
 
for name,lan in f_ls.items():
	#�����ֵ��е�ÿ������ֵ�ԣ��������洢�ڱ���name�У�����ֵ�洢�ڱ���lan��
	print('\n'+name.title()+"'s favorite language is "+
	lan.title()+".")

###��������key ���� keys()
print('\n')
for name in f_ls.keys():
	#��ȡ�ֵ�f_ls�е����м��������ν����Ǵ洢������name��
	print(name.title())
	
print('\n')
for name in f_ls:
	#����key() ��ʵ����ʡ�ԣ������Ͽ�������name����Ϊ����key�ı���
	print(name.title())

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

            
print('\n')
friends = ['phil', 'sarah'] 
for name in f_ls:
	#����f_ls�е�name
	if name in friends:
	#�ж�name�е��ַ��Ƿ����б�friends��
		print("Hi "+name.title()+
		",I see your favorite language is "+
		f_ls[name].title()+"!")

#ʹ��keys()ȷ��ĳ�����Ƿ�����˵���
#���뷽�� key()�����ô���ǽ��ֵ��е�key���ִ��浽ĳ���б���
if 'erin' not in f_ls.keys():
	print("Erin,please take our poll!")

###��˳������ֵ��е�key
f_ls = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print(sorted(f_ls.keys())) 
#���� ֻ����ȷ����ȷʵ��������������б�sorted(f_ls.keys())
#����Ҫ����Ҫ����������м������Ű���
for name in sorted(f_ls.keys()):
	print(name.title()+",thank you!")

###�����ֵ�������value
print(f_ls.values())
#��Ϊ����ֱ�Ӵ�ӡ��������value���б����������Ǳ�������һ��Ĭ�ϵ�dict_values�б�
#�������� ���� ò�Ʋ���
lang = f_ls.values()
print(lang)

print("The following languages have been mentioned:")
for language in f_ls.values():
	print(language.title())

##�޳��ظ��� ����set()
print('\n')
for language in set(f_ls.values()):
	print(language.title())

###6.4Ƕ��

###���б��д����ֵ�
#������˼�ǲ������б���Ƕ���б�������
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2] 
#������һ��Ƕ���������ֵ���б�
for alien in aliens:
    print(alien)

#ʹ��range()���������˲����䴢�����б���
print('\n')
aliens = []
#ʹ��range()������30��һëһ������ɫ������
##����Ҫ�ĺ���
for alien_number in range(30):
	new_alien = {'color':'green','points':5,'speed':'slow'}
	aliens.append(new_alien)
#��ʾǰ���������
for alien in aliens[:5]:
	print(alien)	
print('...')
print('Total number of aliens: '+str(len(aliens)))

#change 
print('\n')
for alien_number in range(30):
	new_alien = {'color':'green','points':5,'speed':'slow'}
	aliens.append(new_alien)
for alien in aliens[0:3]:
	if alien['color'] == 'green':
		alien['color'] == 'yellow'
		alien['speed'] == 'medium'
		alien['points'] == 10
for alien in aliens[:5]:
	print(alien)	
print('...')
print('Total number of aliens: '+str(len(aliens)))		

#��������if-elif ����������������Ҳ�ĵ�


###���ֵ��д洢�б� ����-������һϵ������
#�ʺϣ���һ�������������ֵʱ
# �洢�����������Ϣ
pizza = { 
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }
# ��������ı���
print("You ordered a "+pizza['crust']+"-crust pizza "+
    "with the following toppings:")
for topping in pizza['toppings']: 
	#��ӡ����
    print("\t"+topping)

print(pizza['crust'])
print(pizza['toppings'])

#ʾ��2
f_ls = { 
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }
#Ϊ��һ���Ľ�������򣬿��ڱ����ֵ��forѭ����ͷ����һ��if���
#ͨ���鿴len(languages)��ֵ��ȷ����ǰ�ı�������ϲ���������Ƿ��ж���	
#�����ϲ���������ж��֣�������ǰһ����ʾ���
#���ֻ��һ�֣�����Ӧ�޸�����Ĵ�ǣ�����ʾSarah's favorite language is C
##��� ������ôд������
for name,lans in f_ls.items():
	if len(lans) == 1:
		print(name.title()+"'s favorite language is "+lans[0].title())
		#��Ϊ�б���ֻ��һ��Ԫ�أ����Կ�����lans[0].title()��������ĸ��д
		#.title()���ܶ��б�ʹ��
	else:
		print('\n'+name.title()+"'s farvorite language are:")
		#һֱ������Ϊֹ������ֻ��name
		for lan in lans:
		#������Ҫ�ٱ���һ��lans
			print('\t'+lan.title())

###���ֵ��д洢�ֵ�
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }

print('\n')
for name,infs in users.items():
	print("Username: "+name)
	full_name = infs['first']+''+infs['last']
	location = infs['location']
	print("\tFull name: "+full_name.title())
	print("\tLocation: "+location.title())
##�����ķ�ʽ�����Լ���ģ�������
##�������� infs['first'].title()
print('\n')
for name,infs in users.items():
	print("Username: "+name)
	print("\tFull name: "+infs['first'].title()+' '+infs['last'].title())
	print("\tLocation: "+infs['location'].title())









