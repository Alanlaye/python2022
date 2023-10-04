import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
### 下面是你 with open()函数的相关代码

with open(r"c:\Users\零落\Desktop\python_work\unit_10\pi_digits.txt")  as f:
    contents = f.read()
print(contents)
#关键词with在不需要访问文件后将其关闭
#也可以用open()和close()语句，但是这将导致一些问题

#函数open()接受一个参数：要打开的文件名称('pi_digits)
#函数open()返回一个表示文件的对象(file_objects)

#方法read()将读取文件全部内容
#并将其作为一个长字符串存储在变量contents中；

#FileNotFoundError: [Errno 2] No such file or directory: 'pi_digits.txt'
#文件路径不对
#解决方法：将文件拖到终端，复制地址，修改为： r"文件地址"
#解决方法2：将所有\改为\\或者/
#原理是：单独的\有转义字符的作用

with open(r"c:\Users\零落\Desktop\python_work\unit_10\pi_digits.txt")  as f:
    contents = f.read()
print(contents.rstrip())

#10.1.2 文件路径
#相对路径与绝对路径
#绝对路径需要注意的几个点
#使用反斜杠\
#使用r'文件路径'


#10.1.3 逐行读取
#for 循环
filename = r"c:\Users\零落\Desktop\python_work\unit_10\pi_digits.txt"
with open(filename) as file_object: 
    for line in file_object: 
        print(line.rstrip())

#10.1.4创建一个包含文件各行内容的列表
filename = r"c:\Users\零落\Desktop\python_work\unit_10\pi_digits.txt"
with open(filename) as file_object: 
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())
#方法readlines()从文件中读取每一行并将其存储到一个列表中
#这个列表被存储到变量lines中


#10.1.5 使用文件中的内容
filename = r"c:\Users\零落\Desktop\python_work\unit_10\pi_digits.txt"
with open(filename) as file_object:
    lines = file_object.readlines()
string = ''
for line in lines:
    string += line.strip()
    #每一次输入的line都将作为增添的部分存储到string中
print(string)
print(len(string))

#读取文本文件时，Python将其中的所有文本都解读为字符串
#如果你读取的是数字，并要将其作为数值使用
#就必须使用函数int()将其转换为整数，或使用函数float()将其转换为浮点数

#10.1.6 读取一百万位的大型文件
filename = r"c:\Users\零落\Desktop\python_work\unit_10\pi_digits.txt"
with open(filename) as file_object:
    lines = file_object.readlines()
string = ''
for line in lines:
    string += line.strip()
    #每一次输入的line都将作为增添的部分存储到string中
print(string[:7]+"...")
print(len(string))

#10.1.7 圆周率中包含你的生日吗？
filename = r"c:\Users\零落\Desktop\python_work\unit_10\pi_digits.txt"
with open(filename) as file_object:
    lines = file_object.readlines()
string = ''
for line in lines:
    string += line.strip()

birthday = input("enter you birthday, in the form mmddyy: ")
if birthday in string:
    print("Yes!")
else:
    print("no!")