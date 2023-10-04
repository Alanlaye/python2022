###9.1 创建和使用类

#9.1.1创建Dog类
class Dog(): 
    """一次模拟小狗的简单尝试""" 
    def __init__(self, name, age): 
        """初始化属性name和age"""
        self.name = name 
        self.age = age
    def sit(self): 
        """模拟小狗被命令时蹲下"""
        print(self.name.title()+" is now sitting.")
    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title()+" rolled over!")

#9.1.2根据类创造实例
### my_dog.name表示访问实例my_dog属性

my_dog = Dog('willie',6)
    #访问属性 my_dog.name
print("My dog's name is "+my_dog.name.title()+".")
print("My dog is "+str(my_dog.age)+" years old.")
    #调用方法 my_dog.sit()
my_dog.sit()
my_dog.roll_over()

#创建多个实例
dog_1 = Dog('aa',3)
dog_2 = Dog('bb',5)
dog_1.sit()
dog_2.sit()

###9.2使用类和实例

#9.2.1 Car类
class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year): 
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
    def get_descriptive_name(self): 
        """返回整洁的描述性信息"""
        long_name = str(self.year)+' '+self.make+' '+self.model
        return long_name.title()
my_new_car = Car('audi', 'a4', 2016) 
print(my_new_car.get_descriptive_name())

#9.2.1 Car类
class Car():
    """"一次模拟汽车的简单尝试"""
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    def get_descriptive_name(self):
        """"返回整洁的描述性信息"""
        long_name = str(self.year)+' '+self.make+' '+self.model
        return long_name.title()
car_1 = Car('audi','a4',2016)
    


#9.2.2 给属性指定默认值（初始里程为0）
class Car():
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year)+' '+self.make+' '+self.model
        return long_name.title()
    def read_odometer(self): 
        """打印一条指出汽车里程的消息"""
        print("This car has "+str(self.odometer_reading)+" miles on it.")
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

#9.2.3 修改属性的值

#（1）直接修改
my_new_car.odometer_reading = 23 
#通过实例直接访问属性并赋值修改
my_new_car.read_odometer()

#（2）通过方法修改属性的值
#添加一条方法update_odometer()
class Car():
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year)+' '+self.make+' '+self.model
        return long_name.title()
    def read_odometer(self): 
        """打印一条指出汽车里程的消息"""
        print("This car has "+str(self.odometer_reading)+" miles on it.")
    def update_odometer(self,mileage):
        self.odometer_reading = mileage
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.update_odometer(23)
my_new_car.read_odometer()
#要不找个时间好好看看这几个变量之间的关系
# odometer_reading 

#通过方法对属性的值进行递增