#9-1 餐馆
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print("The restaurant's name is "+self.restaurant_name+".")
        print("Here supply cuisine:"+self.cuisine_type+" .")
    def open_reataurant(self):
        print("Opening now.")


restaurant_1 = Restaurant('aa','bb')
restaurant_1.describe_restaurant()
restaurant_1.open_reataurant()

#9-2 三家餐馆
restaurant_2 = Restaurant('cc','dd')
restaurant_2.describe_restaurant()
restaurant_3 = Restaurant('ee','ff')
restaurant_3.describe_restaurant()

#9-3 User类
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

