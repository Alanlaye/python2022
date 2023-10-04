#9.4.1 导入单个类
#from car import Car:
#第一个小写的car是模块car的名称；第二个Car是Car类

from lesson_3 import Car 
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()


#9.4.2 在一个模块中存储多个类
#将具有相关性的类存储在同一个模块中
from lesson_3 import ElectricCar
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

#9.4.3 从一个模块中导入多个类
from lesson_3 import Car, ElectricCar 
my_beetle = Car('volkswagen', 'beetle', 2016) 
print(my_beetle.get_descriptive_name())
my_tesla = ElectricCar('tesla', 'roadster', 2016) 
print(my_tesla.get_descriptive_name())

#9.4.4 导入整个模块然后使用句点表示法访问需要的类
import car 
my_beetle = car.Car('volkswagen', 'beetle', 2016) 
print(my_beetle.get_descriptive_name())
my_tesla = car.ElectricCar('tesla', 'roadster', 2016) 
print(my_tesla.get_descriptive_name())

#需要从一个模块中导入很多类时
#最好导入整个模块，并使用module_name.class_name语法来访问类

#9.4.5 导入模块中所有类
#代码是：frommodule_name import *

#9.4.6 在一个模块中导入另一个模块

