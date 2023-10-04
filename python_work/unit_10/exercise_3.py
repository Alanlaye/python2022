#10-6 加法运算
print("Enter 2 numbers and I'll tell you the result.")
number_1 = input("the first number: ")
number_2 =input("the second number:")
try:
    result = int(number_1)+int(number_2)
except ValueError:
    print("Please enter in the form of number!")
else:
    result = int(number_1)+int(number_2)
    print(result)

#10-7 加法计算器
while True:
    print("Enter 2 numbers and I'll tell you the result.")
    print("Enter 'q' when you want to break.")

    #为方便用户随时退出
    number_1 = input("the first number: ")
    if number_1 == 'q':
        break
    number_2 =input("the second number:")
    if number_2 == 'q':
        break
    
    #在导致崩溃的代码前使用try_except
    try:
        result = int(number_1)+int(number_2)
    except ValueError:
        print("Please enter in the form of number!")
    else:
        result = int(number_1)+int(number_2)
        print(result)
    
#10-8 猫和狗

filenames = ['cats.txt','dogs.txt']
try:
    for filename in filenames:
        with open(filename) as f:
            contents = f.read()
except FileNotFoundError:
        message = "Sorry, the file "+filename+" does not exist."
        print(message)
else:
        print(contents)
#好崩溃 我居然被同一个bug戏耍了两次
#每次输入File之后会自动弹出来的是FileExistsError
#但是这类错误的名称是FileNotFoundError
        
#10-9 沉默
filenames = ['cats.txt','dogs.txt']
try:
    for filename in filenames:
        with open(filename) as f:
            contents = f.read()
except FileNotFoundError:
        pass
else:
        print(contents)
        
#10-10 常见单词
filename = r"C:\Users\零落\Desktop\python_work\unit_10\lemonade.txt"
with open(filename,'r',encoding='utf-8') as f:
     contents = f.read()
number = contents.lower().count('over')
print(number)

#UnicodeDecodeError:在要打开的文件后面加上
#'r',encoding='utf-8
      
        

