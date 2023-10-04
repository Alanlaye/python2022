###使用类和实例
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
print(car_1.get_descriptive_name())

#9.2.2 给属性指定默认值
#添加一个名为odometer_reading的属性，其初始值总是为0
#为此 编写一个名为read_odometer()的方法
class Car():
    def __init__(self,make,model,year):
        """"初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        #添加一个名为odometer_reading的属性，其初始值为0
    def get_descriptive_name(self):
        """"返回整洁的描述性信息"""
        long_name = str(self.year)+' '+self.make+' '+self.model
        return long_name.title()
    def read_odometer(self):
        """"打印一条指出汽车里程的消息"""
        #只是打印 不做其他
        print("This car has "+str(self.odometer_reading)+" miles on it.")

car_2 = Car('aa','bb',2022)
print(car_2.get_descriptive_name())
car_2.read_odometer()

#9.2.3 修改属性的值


###(1)通过访问属性直接修改属性的值
car_3 = Car('cc','dd',2023)
print(car_2.get_descriptive_name())
car_3.read_odometer()
#上面是原始值
#下面通过访问car_3的属性odometer_reading对其进行赋值
car_3.odometer_reading = 23
car_3.read_odometer()

###（2）通过方法修改属性的值

#原来的创建类的代码 
#我们在read_oddometer()前添加了方法update_odometer()
#方法update_odometer()引入新的形参mile（表示需要获取的实参应该为‘里程数’）
#并将mile中的值存储到self.odometer.reading（属性）中

#def update_odemeter(self,mile):
#""""将里程表度数设定为指定的值"""
#self.odometer_reading = mile

class Car():
    def __init__(self,make,model,year):
        """"初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        #添加一个名为odometer_reading的属性，其初始值为0
    def get_descriptive_name(self):
        """"返回整洁的描述性信息"""
        long_name = str(self.year)+' '+self.make+' '+self.model
        return long_name.title()
    
    def update_odemeter(self,mile):
        """"将里程表度数设定为指定的值"""
        self.odometer_reading = mile
        
    def read_odometer(self):
        """"打印一条指出汽车里程的消息"""
        #只是打印 不做其他
        print("This car has "+str(self.odometer_reading)+" miles on it.")

car_4 = Car('ee','ff',2024)
print(car_4.get_descriptive_name())
car_4.update_odemeter(23)
car_4.read_odometer()
#car_4.update_odemeter(23)
#此处调用该方法，向其提供实参23（对应方法中的形参mile
#接着它将值（23）传递并存储到（self.odometer_reading）中

#（2）拓展——对方法update_odometer()进行扩展
#达成目标：禁止将读数回调
class Car():
    def __init__(self,make,model,year):
        """"初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        #添加一个名为odometer_reading的属性，其初始值为0
    def get_descriptive_name(self):
        """"返回整洁的描述性信息"""
        long_name = str(self.year)+' '+self.make+' '+self.model
        return long_name.title()
    
    def update_odemeter(self,mile):
        """"将里程表度数设定为指定的值"""
        self.odometer_reading = mile
    
    def increment_odometer(self,miles):
        self.odometer_reading += miles
        
    def read_odometer(self):
        """"打印一条指出汽车里程的消息"""
        #只是打印 不做其他
        print("This car has "+str(self.odometer_reading)+" miles on it.")

#(3)通过方法对属性的值进行递增
#新方法increment_ododmeter()接受一个数字（实参）对应mile（形参）
#并将这个实参作为增量叠加到self.odometer_reading中
#通过read_oddmeter()输出
        
        
car_5 = Car('ff','gg',2025)
print(car_5.get_descriptive_name)
car_5.read_odometer()

#直接修改
car_5.odometer_reading = 1000
car_5.read_odometer()

#通过方法修改值的属性
car_5.update_odemeter(2500)
car_5.read_odometer()

#通过方法递增
car_5.increment_odometer(2000)
car_5.read_odometer()
