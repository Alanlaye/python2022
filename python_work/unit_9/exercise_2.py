#9-4 就餐人数
#(1)简单打印及直接访问属性修改
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        """"初始化餐馆名字和菜品"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        """"简要描述餐馆名字和菜品"""
        print("The restaurant's name is "+self.restaurant_name+".")
        print("Here supply cuisine:"+self.cuisine_type+" .")
    def open_reataurant(self):
        """"陈述餐馆营业中"""
        print("Opening now.")
    def serv_numb(self):
        """""打印可接待的就餐人数"""
        if self.number_served == 0 and 1:
            print(str(self.number_served)+" guest has eaten here.")
        else:
            print(str(self.number_served)+" guests have eaten here.")

restaurant_1 = Restaurant('aa','bb')
restaurant_1.describe_restaurant()
restaurant_1.open_reataurant()
restaurant_1.serv_numb()
#访问属性并修改参数
print('m1')
restaurant_1.number_served = 10
restaurant_1.serv_numb()

#（2）使用方法设置就餐人数
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        """"初始化餐馆名字和菜品"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        """"简要描述餐馆名字和菜品"""
        print("The restaurant's name is "+self.restaurant_name+".")
        print("Here supply cuisine:"+self.cuisine_type+" .")
    def open_reataurant(self):
        """"陈述餐馆营业中"""
        print("Opening now.")

    def set_number_served(self,number):
        """""获取客人人数并将其存储到属性中"""
        self.number_served = number

    def serv_numb(self):
        """""打印可接待的就餐人数"""
        if self.number_served == 0 and 1:
            print(str(self.number_served)+" guest has eaten here.")
        else:
            print(str(self.number_served)+" guests have eaten here.")

print('m2')
restaurant_2 = Restaurant('aa','bb')
restaurant_2.set_number_served(20)
restaurant_2.serv_numb() 


#使用方法设置递增人数
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        """"初始化餐馆名字和菜品"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        """"简要描述餐馆名字和菜品"""
        print("The restaurant's name is "+self.restaurant_name+".")
        print("Here supply cuisine:"+self.cuisine_type+" .")

    def open_reataurant(self):
        """"陈述餐馆营业中"""
        print("Opening now.")

    def increment_number_served(self,numbers):
        """""将客人数量作为增量添加到累积接待客人总数（属性）中"""
        self.number_served += numbers

    def serv_numb(self):
        """""打印可接待的就餐人数"""
        if self.number_served == 0 and 1:
            print(str(self.number_served)+" guest has eaten here.")
        else:
            print(str(self.number_served)+" guests have eaten here.")

restaurant_3 = Restaurant('cc','dd')
restaurant_3.increment_number_served(30)
restaurant_3.serv_numb()
restaurant_3.increment_number_served(30)
restaurant_3.serv_numb()


#9-5 尝试登录次数
class User():
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print("first_name:"+self.first_name.title())
        print("last_name:"+self.last_name.title())
        print("age:"+str(self.age))

    def incremend_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def greet_user(self):
        print("Hello, "+self.first_name+" "+self.last_name+"!")

user_1 = User('aa','bb',17)
print(user_1.login_attempts)
user_1.incremend_login_attempts()
while True:
    user_1.incremend_login_attempts()
    if user_1.login_attempts >= 30:
        print("You've tried so many time!")
        break
print(user_1.login_attempts)
user_1.incremend_login_attempts()
print(user_1.login_attempts)

user_1.reset_login_attempts()
print(user_1.login_attempts)