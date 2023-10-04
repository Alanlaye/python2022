#传递任意数量的（位置）实参:星号 *toppings
def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

#完善描述
def make_pizza(*toppings):
    """"描述披萨"""
    print("\nMakeing a pizza with the following toppings:")
    for topping in toppings:
        print(topping)
    
make_pizza('aa')
make_pizza('aa','bb','cc')

#8.5.1结合使用位置实参和任意数量实参
def make_pizza(size,*toppings):
    """"概述披萨"""
    print("\nMaking a "+str(size)+"-pizza with the following toppings:")
    for topping in toppings:
        print(topping)
make_pizza(16,'aa')
make_pizza(19,'aa','bb','cc')

#8.5.2使用任意数量的关键字实参
#形参**user_info中的两个星号让Python创建一个名为user_info的空字典
def build_profile(first,last,**user_info):
    """"创建字典，封装有关用户的实参"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('aa','bb',location='cc',age = 14)
print(user_profile)