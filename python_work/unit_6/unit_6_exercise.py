#coding=utf-8
#6.2 ��Ӻ�ɾ���ֵ�
alanlaye = {'f_n':'alan','l_n':'laye','age':19,'city':'tokyo'}
print(alanlaye['f_n'].title())
print(alanlaye['l_n'].title())
print(alanlaye['age'])
print(alanlaye['city'].title())
#printѯ�ʻ���
flo_number = {'Calla':3,'lily':4,'carnation':5,'daisy':7,'iris':9}
flo=['Calla','lily','carnation','daisy','iris']
print(flo_number)
print('Calla,do you like '+ str(flo_number['Calla'])+'?')

#6.3 �����б�
#��ӡkey-value��
for k,v in flo_number.items():
	print("\nKey:"+k+";"+"Value:"+str(v))

r_c = {'nile':'egypt','mississippi':'usa','changjiang':'china'}
for r,c in r_c.items():
	print("The "+r.title()+" runs through "+c.title()+".")
for r in r_c.keys():
	print(r.title())
for c in r_c.values():
	print(c.title())
#������һ������������飬�ող����İ�c�����v ���Ǿ�Ȼ������� ���Ϊchina Ϊʲô

#����
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
	
	
#6.4Ƕ��
#��
alanlaye = {'f_n':'alan','l_n':'laye','age':19,'city':'tokyo'}
izakkull = {'f_n':'izakku','l_n':'ll','age':17,'city':'beijing'}
alexhers = {'f_n':'alex','l_n':'hers','age':21,'city':'marchtown'}
people = [alanlaye,izakkull,alexhers]
for person in people:
	print(person)
#���� ��ôͨ�������б���һ����Ȼ���ָ��Alanlaye��ȫ����Ϣ
#���磺Alanlaye's full-name is Alanlaye,her age is 19,she lives in tokyo.
#Ϊʲô���������Ĵΰ�()
for peo in people:
	for k,v in peo.items():
		print('Full name = '+peo['f_n']+peo['l_n'])
		print('Age = '+str(peo['age']))
		print('City = '+peo['city'])
#����2


#��������������Ƕ�����б��е��ֵ䡪������������
#���ǽ̳���Ҳû��
aa = {'type':'dog','master':'alan'}
bb = {'type':'cat','master':'laye'}
cc = {'type':'lion','master':'alex'}
pets = []
pets.append(aa)
pets.append(bb)
pets.append(cc)
print(pets)
for pet in pets:
	#�ⲽ��Ҫ��aa bb cc ���������� ��������pet��
	for key,value in pet.items():
		#�ֱ����aabbcc�е�key-value
		print(key.title()+':'+str(value).title())
#�ߺ� �����ټ�һ��'name':'aa'֮���
#�����б����Բ������ֵ������� for k,v in pets.items()

#ϲ���ĵط�
f_ps = {
	'aa':['usa','uk','cn'],
	'bb':['jp','uk','fr'],
	'cc':['ru','sp','kr'],
	}
for key,value in f_ps.items():
	print(key+'favorite places are: ')
	print(value)
#�ȵ� ��Ϊvalue��һ���б� ����ֻ�ܵ������������print(value)

#ϲ��������
flo_number = {
	'calla':[3,4],
	'lily':[4,5],
	'iris':[6,9],
	}
for key,value in flo_number.items():
	print(key+'favorite_number are: ')
	for number in value:
		#���갡 ԭ����Ҫ������ ������б�ͼӸ�����Ȼ�����
		#������ֵ�����������print(value['iris'])
		print(number)
#�������ͬ��Ƕ�����ֵ��е��б���Ϊvalue���ʱ����Ҫ��������������ܺ�printһ��
#���ʵ����Ҫһ�����һ�������������Խ��䴢���ĳһ������

#Ƕ�����ֵ��е��ֵ� ����
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
#��ʵ�Ҹ���֪��������ôȥ����Щ�����ֵ�Ļ�����
#�������Ȼ����	
#�Ҳ� �Ҿ�Ȼ������������� ��������Ϊʲô��
#city��infs ��ʵ���Ա�������Ϊһ���б��һ���ֵ�		
print('\n')
for city,infs in cities.items():
	print('City:'+city)
	print('Country:'+infs['coun'])
	print('Population'+str(infs['popu']))
	print('Fact'+infs['fact'])





	


	
	
	


