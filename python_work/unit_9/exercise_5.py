#exercise_5
#9-13
from collections import OrderedDict
favorite_flowers = OrderedDict()
favorite_flowers['aa'] = 'bb'
favorite_flowers['cc'] = 'dd'

for name,flower in favorite_flowers.items():
    print(name.title()+"'s favorite flower is "+flower+".")

 #9-14
    
from random import randint
class Die():
    def __init__(self,sides):
        self.sides = sides
    
    def roll_sides(self):
        for i in range(10):
            print(randint(1, self.sides), end=" ")
    

die_1 = Die(6)
die_1.roll_sides()

die_2 = Die(12)
die_2.roll_sides()

#有两个问题
#第一：这个for_in range(10)的语句含义到底是什么
#答案：某个操作重复执行指定次数
#第二：为什么明明有三个实例调用了三次方法 但只显示最后一个


    







