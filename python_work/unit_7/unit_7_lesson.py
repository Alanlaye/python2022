###7.1 函数input()获取用户输入字符串
#示例1
message = input('Tell me something,and I will repeat it back to you: ')
print(message)
#input()中填写描述性语句+一个冒号+空格
#用户在空格中输入的信息将被存储在变量message中
#示例2
name = input('Please enter your name: ')
print('Hello, '+name+'!')
#示例3
prompt = 'If you tell us who you are,we can personalize the message you see.'
prompt+= '\nWhat is your first name? '
#运算符+=在存储在prompt中的字符串末尾附加一个字符串
name = input(prompt)
#因为提示过长所以先将其存储在变量prompt中，此时input语句会显得简洁
print('\nHello, '+name+'!')

##7.1.2使用int()获取数值输入
age = input("How old are you? ")
print(int(age) > 18)
#对于列表输出将字符串变成数字有函数str()
#对于用户输入则是函数int()
##示例：判断过山车与年龄
height = input("How tall are you, in inches? ")
height = int(height)
if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

##7.1.3求模运算符（%）
#它将两个数相除并返回余数
print(4 % 3)
#如果一个数可被另一个数整除，余数就为0，因此求模运算符将返回0
#你可利用这一点来判断一个数是奇数还是偶数
#示例：even_or_odd
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print("The number "+str(number)+" is even.")
else:
    print("The number "+str(number)+" is odd.")

###7.2 while循环
number = 1
while number <= 5:
    print(number)
    number += 1
    #只是测试了一下空格随意
#7.2.2 让用户选择何时推出
prompt = "\nTell me something, and I will repeat it back to you:" 
prompt+= "\nEnter 'quit' to end the program. "
#prompt+表示将两个字符串连接在一起
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)
#发现问题：最后quit时会将quit再输出 想想循环的过程
#可以和上面的number比较 发现与print和变量的顺序有关
#优化策略1：调整顺序（但是比较脱离现实逻辑）
prompt = "\nTell me something, and I will repeat it back to you:" 
prompt+= "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    print(message)
    message = input(prompt)
#优化策略2：使用if测试
prompt = "\nTell me something, and I will repeat it back to you:" 
prompt+= "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        #此处的if判断起到限制最后一次输出的作用
        print(message)

#7.2.3 使用标志 （将测试外置于while循环）
print('New')
prompt = "\nTell me something, and I will repeat it back to you:" 
prompt+= "\nEnter 'quit' to end the program. "
active = True   
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

#7.2.4 使用break语句退出（任何）循环
#while True后一定要接break
prompt = "\nPlease enter the name of a city you have visited:"
prompt+= "\n(Enter 'quit' when you are finished.) "
while True: 
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to "+city.title()+"!") 

#7.2.5在循环中使用continue
#打印1-10内所有奇数
number = 0
while number < 10:
    number += 1
    if number % 2 == 0:
        continue
    print(number)
#打印1-10内所有偶数
number = 1
while number <= 10:
    number += 1
    if number % 2 != 0:
        continue
    else:
        print(number)
    
#7.2.6避免无限循环
#确认程序至少有一个这样的地方能让循环条件为False或让break语句得以执行


###7.3 使用while循环处理列表与字典 
#7.3.1在列表间移动元素
# 首先，创建一个待验证用户列表和一个用于存储已验证用户的空列表
unconfirmed_users = ['alice', 'brian', 'candace'] 
confirmed_users = []
# 验证每个用户，直到没有未验证用户为止
#  将每个经过验证的列表都移到已验证用户列表中
while unconfirmed_users: 
    current_user = unconfirmed_users.pop() 
    print("Verifying user: "+current_user.title())
    confirmed_users.append(current_user) 
# 显示所有已验证的用户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

#7.3.2 删除包含特定值的所有列表元素
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
while 'cat' in pets:
    pets.remove('cat')
print(pets)

#7.3.3 使用用户输入来填充字典
responses = {}
# 设置一个标志，指出调查是否继续
polling_active = True
while polling_active:
    # 提示输入被调查者的名字和回答
    name = input("\nWhat is your name? ") 
    response = input("Which mountain would you like to climb someday? ")
    # 将答卷存储在字典中
    responses[name] = response 
    # 看看是否还有人要参与调查
    repeat = input("Would you like to let another person respond? (yes/ no) ") 
    if repeat == 'no':
        polling_active = False
# 调查结束，显示结果
print("\n--- Poll Results ---")
for name, response in responses.items(): 
    print(name+" would like to climb "+response+".")
