#coding=utf-8
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
print(bicycles[0].title())

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1])
print(bicycles[-2].title())

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message='My first bicycle was a '+bicycles[0].title()+'.'
print(message)

#1 ����
names=['alan','laye','Izakku']
print(names[0])
print(names[1])
print(names[2])
#ֻ������һ���ܲ���һ�����б�ȫ��title(),���ǲ��ܣ�Ȼ�󲻸��ĵ�ȫ������title��һ�飨��
print(names[0].title())
print(names[1].title())
print(names[2].title())

#2 �ʺ��� ��Ϸ�����ֶ���ҽ�ɫ�ʺŵĴ����������д���𣿵���һ��һ��������鷳����û�����ֿ���һ����ѡ������Ĵ��룿
names=['alan','laye','Izakku']
message=names[0].title()+',good morning!'
names[0]=message
print(names[0])

names=['alan','laye','Izakku']
message=names[1].title()+',good morning!'
names[1]=message
print(names[1])

names=['alan','laye','Izakku']
message=names[2].title()+',good morning!'
names[2]=message
print(names[2])

#3 �Լ����б�
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
names=['alan','laye','Izakku']
message=names[0].title()+' would like to own a '+bicycles[0]+'!'
print(message)

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
names=['alan','laye','Izakku']
message=names[1].title()+' would like to own a '+bicycles[1]+'!'
print(message)
