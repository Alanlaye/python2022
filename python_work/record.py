#coding=utf-8
alanlaye = {'f_n':'alan','l_n':'laye','age':19,'city':'tokyo'}
izakkull = {'f_n':'izakku','l_n':'ll','age':17,'city':'beijing'}
alexhers = {'f_n':'alex','l_n':'hers','age':21,'city':'marchtown'}
people = [alanlaye,izakkull,alexhers]
for peo in people:
	print('Full name = '+peo['f_n']+peo['l_n'])
	print('Age = '+str(peo['age']))
	print('City = '+peo['city'])
#已经使用了 for k,v in peo.items()，为什么后面还要使用peo去调取字典？
#这样的话k和v完全没有用到，循环的次数等于字典的键值个数
#上面是第一种改法
#如果我一定要用for k,v in peo.items()的话
#该怎么把v的值挨个打出来呢——遍历字典
for peo in people:
	for k,v in peo.items():
		print(k)
		
