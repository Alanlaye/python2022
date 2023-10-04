###定义函数 def

#函数名是greet_user()
#括号中是函数为完成任务所需要的信息 但也可以不需要信息
#需要以冒号结尾
#三引号中间是docstring的注释
#这个函数只做一项工作：打印Hello！
def greet_user():
    """"显示简单问候语"""
    print("Hello！")
greet_user()

#8.1.1向函数传递信息
def greet_user(name):
    print("Hello, "+name.title()+"!")
greet_user('izakku')

#8.1.2 实参和形参
#形参——函数完成其工作所需的一项信息（name）
#实参——调用函数时传递给函数的信息（'izakku')


#8.2.1位置实参(顺序)
#调用函数多次
def describe_pet(animal_type, pet_name): 
    """显示宠物的信息"""
    print("\nI have a "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")
describe_pet('hamster', 'harry') 
#位置实参的顺序很重要

#8.2.2关键字实参
#name-value
#name(形参)；value（实参）
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")
describe_pet(animal_type = 'hamster', pet_name = 'harry')

#8.2.3默认值
#如果你发现调用describe_pet()时，描述的大都是小狗
#就可将形参animal_type的默认值设置为'dog'
def describe_pet(pet_name,animal_type = 'dog'):
    """"显示宠物信息"""
    print("\nI have a "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")
describe_pet(pet_name = 'while')
#使用默认值时，在形参列表中必须先列出没有默认值的形参，再列出有默认值的形参
#因为Python依然将这个只有一个的实参视为位置实参

#8.2.4等效的函数调用
def describe_pet(pet_name, animal_type='dog'):
    # 一条名为Willie的小狗
    describe_pet('willie')
    #位置实参
    describe_pet(pet_name='willie')
    #关键字实参

    # 一只名为Harry的仓鼠
    describe_pet('harry', 'hamster')
    #位置实参
    describe_pet(pet_name='harry', animal_type='hamster')
    describe_pet(animal_type='hamster', pet_name='harry')
    #关键字实参


###8.3 返回值
#8.3.1 返回简单值
def get_formatted_name(first_name, last_name): 
    full_name = first_name+' '+last_name 
    return full_name.title()
musician = get_formatted_name('jimi','hers')
print(musician)

#8.3.2 让实参变为可选的
#先扩展（背景）
def get_formatted_name(first_name, middle_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name+' '+middle_name+' '+last_name
    return full_name.title()
musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

#为让get_formatted_name()在没有提供中间名时依然可行
#可给实参middle_name指定一个默认值——空字符串，并将其移到形参列表的末尾
def get_formatted_name(first_name, last_name,middle_name = ''):
    if middle_name:
        #检查是否提供了中间名,Python将非空字符串解读为True
        #完整写法应该是if middle_name != '':
        full_name = first_name+' '+middle_name+' '+last_name
    else:
        full_name = first_name+' '+last_name
    return full_name.title()
musician = get_formatted_name('jimi','hers')
print(musician)
musician = get_formatted_name('john','hooker','lee')
print(musician)

#8.3.2 返回字典
def build_person(first_name, last_name):
    """返回一个字典，其中包含有关一个人的信息"""
    #需要获取first_name和last_name并将其封装在字典中
    person = {'first': first_name, 'last': last_name} 
    return person 
musician = build_person('jimi', 'hendrix')
print(musician) 

def build_person(first_name,last_name,age = ''):
    person = {'first':first_name,'last':last_name,'age':''}
    if age:
        person['age'] = age
        return person
musician = build_person('jimi', 'hendrix',27)
print(musician) 

#8.3.4 结合使用函数和while循环
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name+' '+last_name
    return full_name.title()
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    first_name = input("First name: ")
    if first_name == 'q':
        break
    last_name = input("Last name: ")
    if last_name == 'q':
        break
    formatted_name = get_formatted_name(first_name, last_name)
    print("\nHello, "+formatted_name+"!")
#其实最严重的问题是那么多变量
#first_name,last_name作为形参，提示函数需要的信息，存储实参
#full_name是函数体内操作信息的变量，被返还存储到formatted_name中
#f_name,l_name分别用来存储通过input获得的实参（第一次），然后传递给形参
##但是多此一举，完全可以直接用first_name,last_name来存储 反正要存储的东西是一样的
#（这是我自己想的，不一定对，后面可以验证） 