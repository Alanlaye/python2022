#coding=utf-8
#6.2 添加和删改字典
alanlaye = {'f_n':'alan','l_n':'laye','age':19,'city':'tokyo'}
print(alanlaye['f_n'].title())
print(alanlaye['l_n'].title())
print(alanlaye['age'])
print(alanlaye['city'].title())
#print询问环节
flo_number = {'Calla':3,'lily':4,'carnation':5,'daisy':7,'iris':9}
flo=['Calla','lily','carnation','daisy','iris']
print(flo_number)
print('Calla,do you like '+ str(flo_number['Calla'])+'?')

#6.3 遍历列表
#打印key-value对
for k,v in flo_number.items():
	print("\nKey:"+k+";"+"Value:"+str(v))

r_c = {'nile':'egypt','mississippi':'usa','changjiang':'china'}
for r,c in r_c.items():
	print("The "+r.title()+" runs through "+c.title()+".")
for r in r_c.keys():
	print(r.title())
for c in r_c.values():
	print(c.title())
#但是有一个很神奇的事情，刚刚不下心把c打成了v 但是居然可以输出 输出为china 为什么

#调查
f_ls = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
	
should = ['jen','sarah','izakku','alan','phil']	
for people in should:
	if people in f_ls.keys():
		print(people.title()+' thank you!')
	else:
		 print(people.title()+' Welcome!')
	
	
#6.4嵌套
#人
alanlaye = {'f_n':'alan','l_n':'laye','age':19,'city':'tokyo'}
izakkull = {'f_n':'izakku','l_n':'ll','age':17,'city':'beijing'}
alexhers = {'f_n':'alex','l_n':'hers','age':21,'city':'marchtown'}
people = [alanlaye,izakkull,alexhers]
for person in people:
	print(person)
#不是 怎么通过遍历列表用一个自然语句指出Alanlaye的全部信息
#比如：Alanlaye's full-name is Alanlaye,her age is 19,she lives in tokyo.
#为什么这个会输出四次啊()
for peo in people:
	for k,v in peo.items():
		print('Full name = '+peo['f_n']+peo['l_n'])
		print('Age = '+str(peo['age']))
		print('City = '+peo['city'])
#方法2


#宠物——这个问题是嵌套在列表中的字典——带入外星人
#但是教程上也没提
aa = {'type':'dog','master':'alan'}
bb = {'type':'cat','master':'laye'}
cc = {'type':'lion','master':'alex'}
pets = []
pets.append(aa)
pets.append(bb)
pets.append(cc)
print(pets)
for pet in pets:
	#这步是要把aa bb cc 三个调出来 调进变量pet中
	for key,value in pet.items():
		#分别调出aabbcc中的key-value
		print(key.title()+':'+str(value).title())
#哼哼 大不了再加一个'name':'aa'之类的
#这是列表，所以不能像字典那样用 for k,v in pets.items()

#喜欢的地方
f_ps = {
	'aa':['usa','uk','cn'],
	'bb':['jp','uk','fr'],
	'cc':['ru','sp','kr'],
	}
for key,value in f_ps.items():
	print(key+'favorite places are: ')
	print(value)
#等等 因为value是一个列表 所以只能单独输出类似于print(value)

#喜欢的数字
flo_number = {
	'calla':[3,4],
	'lily':[4,5],
	'iris':[6,9],
	}
for key,value in flo_number.items():
	print(key+'favorite_number are: ')
	for number in value:
		#尼玛啊 原来是要这样做 想遍历列表就加个变量然后输出
		#想遍历字典更多情况下是print(value['iris'])
		print(number)
#和上面的同理，嵌套在字典中的列表作为value输出时，需要单独输出，而不能和print一起
#如果实在需要一起放入一个句子里，或许可以将其储存进某一个变量

#嵌套在字典中的字典 城市
cities = {
	'sz':{
		'coun':'cn',
		'popu':100,
		'fact':'mordern',
		},
	'mg':{
		'coun':'tg',
		'popu':50,
		'fact':'yammy',
		},
	}
#其实我更想知道的是怎么去掉这些代表字典的花括号
#而输出自然语言	
#我擦 我居然真的做到了呃呃 但是这是为什么呢
#city和infs 其实各自被调出作为一个列表和一个字典		
print('\n')
for city,infs in cities.items():
	print('City:'+city)
	print('Country:'+infs['coun'])
	print('Population'+str(infs['popu']))
	print('Fact'+infs['fact'])





	


	
	
	


