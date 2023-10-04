#8-12 三明治
def  make_sandwich(*toppings):
    print("\nMaking a sandwich with these toppings:")
    for topping in toppings:
        print(topping)

make_sandwich('aa')
make_sandwich('bb','cc')
make_sandwich('cc','ff','tt')

#8-13用户简介
def user_profile(first,last,**infos):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in infos.items():
        profile[key] = value
    return profile

alanlaye = user_profile('alan','laye',age = 17,city = 'tokyo')
print(alanlaye)

#8-14 汽车
def make_car(firm,type,**infs):
    car = {}
    car['firm'] = firm
    car['type'] = type
    for key,value in infs.items():
        car[key] = value
    return car
def show_car(firm,type,**infs):
    print("Here are some details about the car:")
    for fi in firm:
        print("Firm:"+fi)
    for ty in type:
        print("Type:"+ty)
    for key,value in infs.items():
        print(key.title()+":"+value)

car_1 = make_car('aa','bb',color = 'cc',dd = 'ee')
car_1_show = show_car('aa','bb',color = 'cc',dd = 'ee')