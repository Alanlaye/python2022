#10.3.2 try_except 代码块
#返回友好的错误消息而非traceback
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

#10.3.3 使用异常避免崩溃
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    
    try: 
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError: 
        print("You can't divide by 0!")
    
    else: 
        answer = int(first_number) / int(second_number)
        print(answer)

#10.3.5 处理FileNotFoundError异常
filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file "+filename+" does not exist."
    print(msg)

#10.3.6分析文本
title = "Alice in Wonderland"
print(title.split())

filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    message = "Sorry,the file "+filename+" does not exist."
    print(message)
else:
    words = contents.split()
    #方法split()将长字符串contents根据空格拆成多个字符串
    #并将其存储在列表words
    num_words = len(words)
    #计算列表长度
    print("The File "+filename+" has about "+str(num_words)+" words.")


#10.3.7 使用多个文件
#先将单个文本分析的程序转移到函数count_words()中

def count_words(filename):
    """计算一个文件大致包含多少个单词""" 
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file "+filename+" does not exist."
        print(msg)
    else:
        # 计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print("The file "+filename+" has about "+str(num_words)+
            " words.")
        
filename = 'alice.txt'
count_words(filename)

#使用函数处理多个文本
filenames = ['aa.txt','bb.txt','cc.txt']
for filename in filenames:
    count_words(filename)

#10.3.8 pass语句
def count_words(filename):
    """计算一个文件大致包含多少个单词""" 
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        # 计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print("The file "+filename+" has about "+str(num_words)+
            " words.")