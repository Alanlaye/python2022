#coding=utf-8
alanlaye = {'f_n':'alan','l_n':'laye','age':19,'city':'tokyo'}
izakkull = {'f_n':'izakku','l_n':'ll','age':17,'city':'beijing'}
alexhers = {'f_n':'alex','l_n':'hers','age':21,'city':'marchtown'}
people = [alanlaye,izakkull,alexhers]
for peo in people:
	print('Full name = '+peo['f_n']+peo['l_n'])
	print('Age = '+str(peo['age']))
	print('City = '+peo['city'])
#�Ѿ�ʹ���� for k,v in peo.items()��Ϊʲô���滹Ҫʹ��peoȥ��ȡ�ֵ䣿
#�����Ļ�k��v��ȫû���õ���ѭ���Ĵ��������ֵ�ļ�ֵ����
#�����ǵ�һ�ָķ�
#�����һ��Ҫ��for k,v in peo.items()�Ļ�
#����ô��v��ֵ����������ء��������ֵ�
for peo in people:
	for k,v in peo.items():
		print(k)
		
