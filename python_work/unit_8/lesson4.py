#8.4 传递列表
def greet_users(names):
    """向列表中的每位用户都发出简单的问候"""
    for name in names:
        msg = "Hello, "+name.title()+"!"
        print(msg)
names = ['hannah', 'ty', 'margot'] 
greet_users(names)

#8.4.1 在函数中修改列表

#不使用函数：
# 首先创建一个列表，其中包含一些要打印的设计
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
# 模拟打印每个设计，直到没有未打印的设计为止
#  打印每个设计后，都将其移到列表completed_models中
while unprinted_designs:
    current_design = unprinted_designs.pop()
    #模拟根据设计制作3D打印模型的过程
    print("Printing model: "+current_design)
    completed_models.append(current_design)
# 显示打印好的所有模型
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

#使用函数：
def print_models(un_m,co_m):
    while un_m:
        cu_m = un_m.pop()
        print("Printing model: "+cu_m)
        co_m.append(cu_m)
def show(co_m):
    print("\nThe following models have been printed:")
    for co in co_m:
        print(co)
un_m = ['iphone case', 'robot pendant', 'dodecahedron']
co_m = []
print_models(un_m,co_m)
show(co_m)

#补充：原书中的代码
def print_models(unprinted_designs, completed_models): 
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表completed_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # 模拟根据设计制作3D打印模型的过程
        print("Printing model: "+current_design)
        completed_models.append(current_design)
def show_completed_models(completed_models): 
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

###每个函数都应只负责一项具体的工作

#8.4.2 禁止函数修改列表
#向函数传递列表的副本而不是原件
#切片表示法[:]创建列表的副本
#如果不想清空未打印的设计列表，可像下面这样调用print_models()
#【之前是这样】
# def print_models(unprinted_designs, completed_models): 
#【现在可以这样】
# def print_models(unprinted_designs, completed_models): 

#不过还是建议使用原始列表 