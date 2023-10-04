#9-6 冰淇淋小店
#冰淇淋店是一种特殊的餐馆
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print("The restaurant's name is "+self.restaurant_name+".")
        print("Here supply cuisine:"+self.cuisine_type+" .")
    def open_reataurant(self):
        print("Opening now.")


class IceCreamStand(Restaurant):
    """IceCreamStand的独特之处"""
    def __init__(self,restaurant_name,cuisine_type,*flavors):
        """初始化父类的属性"""
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = flavors
    def flavors_show(self):
        print("We have the following flavors: ")
        for self.flavor in self.flavors:
            print(self.flavor)


        
restaurant = Restaurant('cc','dd')
restaurant.describe_restaurant()

ice_1 = IceCreamStand('aa','bb')    
ice_1.describe_restaurant()

ice_2 = IceCreamStand('cc','dd','ee','ff','gg')
ice_2.flavors_show()
#在属性flavors前面加星号，实参传入进去之后会变成元组

#9-7 管理员
#：管理员是一种特殊的用户
class User():
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def describe_user(self):
        print("first_name:"+self.first_name.title())
        print("last_name:"+self.last_name.title())
        print("age:"+str(self.age))
    def greet_user(self):
        print("Hello, "+self.first_name+" "+self.last_name+"!")
        
user_1 = User('aa','bb',17)
user_1.describe_user()
user_1.greet_user()

class Admin(User):
    def __init__(self, first_name, last_name, age,*priviliges):
        super().__init__(first_name, last_name, age)
        self.privileges = priviliges

    def show_privileges(self):
        print("Admin have the following privileges: ")
        for self.privilege in self.privileges:
            print(self.privilege)

admi_1 = Admin('aa','bb',18,"can add post","can delete post","can ban user")
admi_1.show_privileges()

#9-8
class Privileges():
    def __init__(self,privileges = ["can add post","can delete post","can ban user"]):
        #如果要设定默认值的话，直接在初始化代码行设置
        self.privileges =privileges

    def show_priviliges(self):
        print("Admin have the following privileges: ")
        for self.privilege in self.privileges:
            print(self.privilege)

pre_1 = Privileges([])
#自然是放空列表打印默认值啦——此处需要用到的知识是设定默认值和修改默认值
pre_1.show_priviliges()

#将Privileges实例作为Admi的一个属性
class Admi(User):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privileges = Privileges()

admi_2 = Admi('ee','ff',19,)
admi_2.describe_user()
admi_2.greet_user()
admi_2.privileges.show_priviliges()

#9-9 电瓶升级
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

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85


class ElectricCar(Car):
    def __init__(self, make, model, year):
        """
        电动汽车的独特之处
        初始化父类的属性，再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)
        self.battery_size = 70 
        self.battery = Battery()
    
    def fill_gas_tank(self):
        """""电动汽车没有邮箱"""
        print("This car doesn't need a gas tank!")

        
elec = ElectricCar('aa','bb','cc')
elec.fill_gas_tank()
elec.battery.get_range()
elec.battery.upgrade_battery()
elec.battery.get_range()
