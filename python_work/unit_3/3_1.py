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

#1 姓名
names=['alan','laye','Izakku']
print(names[0])
print(names[1])
print(names[2])
#只是想试一下能不能一次性列表全部title(),答案是不能，然后不甘心地全部单独title了一遍（）
print(names[0].title())
print(names[1].title())
print(names[2].title())

#2 问候语 游戏中那种对玩家角色问号的代码就是这样写的吗？但是一个一个输入好麻烦，有没有那种可以一次性选择调出的代码？
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

#3 自己的列表
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
names=['alan','laye','Izakku']
message=names[0].title()+' would like to own a '+bicycles[0]+'!'
print(message)

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
names=['alan','laye','Izakku']
message=names[1].title()+' would like to own a '+bicycles[1]+'!'
print(message)
