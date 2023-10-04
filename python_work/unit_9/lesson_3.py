#9.3 继承
###9.3 继承
#9.3.1 子类的方法__init__()
class Car(): 
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year)+' '+self.make+' '+self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading+= miles

class ElectricCar(Car): 
    """电动汽车的独特之处"""
    def __init__(self, make, model, year): 
        """初始化父类的属性"""
        super().__init__(make, model, year) 

my_tesla = ElectricCar('tesla', 'model s', 2016) 
print(my_tesla.get_descriptive_name())
#其实上面的代码只是测试ElectricCar作为普通Car的一般行为
#并没有定义独特之处
#所以其实只有两个特殊的点需要注意：
#class ElectricCar(Car):
#初始化父类属性 super().__int__(make,model,year)

#9.3.3 给子类定义属性和方法
#示例：电动汽车的battery(属性)
class ElectricCar(Car):
    def __init__(self, make, model, year):
        """
        电动汽车的独特之处
        初始化父类的属性，再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)
        self.battery_size = 70 

    def describe_battery(self): 
        """打印一条描述电瓶容量的消息"""
        print("This car has a "+str(self.battery_size)+"-kWh battery.")
electice_1 = ElectricCar('tesla', 'model s', 2016)
print(electice_1.get_descriptive_name())
electice_1.describe_battery()

#9.3.4 重写父类的方法
#可在子类中定义一个这样的方法，即它与要重写的父类方法同名
#这样，Python将不会考虑这个父类方法，而只关注你在子类中定义的相应方法
class ElectricCar(Car):
    def __init__(self, make, model, year):
        """
        电动汽车的独特之处
        初始化父类的属性，再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)
        self.battery_size = 70 
    
    def fill_gas_tank(self):
        """""电动汽车没有邮箱"""
        print("This car doesn't need a gas tank!")

electric_2 = ElectricCar('cc','dd',2022)
electric_2.fill_gas_tank()

#9.3.5 将实例用作属性

#此处有class Car():略

#编写关于电瓶的类：属性主要是battery_size
class Battery():
    """""模拟电瓶"""
    def __init__(self,battery_size=70):
        self.battery_size = battery_size
    def describe_battery(self):
        """""电瓶规模"""
        print("This car has a "+str(self.battery_size)+"=kWh battery")
    def get_range(self):
        """""续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately "+str(range)
        message += " miles on a full charge."
        print(message)


#将Battery实例存储到self.battery中，作为ElectriCar类的属性
class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()
        #Battery()意味着创建一个新的Battery实例

electice_3 = ElectricCar('ee','ff',2020)
print(electice_3.get_descriptive_name)
electice_3.battery.describe_battery()
#这行代码让Python在实例electice_3中查找属性battery
#并对存储在该属性中的Battery实例调用方法describe_battery()
electice_3.battery.get_range()
