#10.4.1 使用json.dump()和json.load()
import json
numbers = [2, 3, 5, 7, 11, 13]
filename = r'C:\Users\零落\Desktop\python_work\unit_10\numbers.json' 

with open(filename, 'w') as f_obj: 
    json.dump(numbers, f_obj) 
    #json.dump() 将数据存储到文件中

    
import json
with open(file='numbers.json',mode='r',encoding='utf-8',errors='ignore') as f:
    numbers = json.load(f)
    #json.load()则将数据从文件中载入python程序
print(numbers)


#10.4.2 保存和读取用户生成的数据
import json
# 如果以前存储了用户名，就加载它
# 否则，就提示用户输入用户名并存储它

filename = 'username.json'
try:
    with open(filename) as f_obj: 
        username = json.load(f_obj)
        #首次运行时并不存在这个文件将引发异常
        #接着执行except代码块
except FileNotFoundError: 
    username = input("What is your name? ") 
    with open(filename, 'w') as f_obj: 
        json.dump(username, f_obj)
        print("We'll remember you when you come back, "+username+"!")
        #第二次之后用户再次运行程序时将不会引发异常，直接执行else代码块
else:
    print("Welcome back, "+username+"!")


#10.4.3 重构
#remember_me.py
#原始函数（做两个任务）
import json
def greet_user():
    """问候用户，并指出其名字""" 
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you when you come back, "+username+"!")
    else:
        print("Welcome back, "+username+"!")
greet_user()

#重构greet_user() 使每个函数只执行一个任务
import json
def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username
    
def get_new_username():
    username = input("What's your name? ")
    filename = 'username.json'
    with open(filename,'w') as f:
        json.dump(username,f)
    return username

def greet_user():
    username = get_stored_username()
    if username:
        check = input("Is "+username+" your name?(y/n: ")
        if check == y:
            print("Welcome back, "+username+"!")
        else:
            username = get_new_username()
            print("We'll remember you when you come back, "+username+"!")   
    else:
        username = get_new_username()
        print("We'll remember you when you come back, "+username+"!")

