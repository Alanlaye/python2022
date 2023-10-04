#10.2 写入文件

#10.2.1 写入空文件
filename = r"c:\Users\零落\Desktop\python_work\unit_10\pi_digits.txt"
with open(filename,'w') as file_object:
    file_object.write("I love programming")
#向open()提供的两个实参：filename和'w'，分别代表打开文件名称和写入模式
#打开文件时，可指定读取模式（'r'）、写入模式（'w'）、附加模式（'a'）
#或让你能够读取和写入文件的模式（'r+'）
#'w'写入模式将在返回文件对象前清空该文件以写入
#要将数值数据存储到文本文件中，必须先使用函数str()将其转换为字符串格式

#10.2.2 写入多行
filename = r"c:\Users\零落\Desktop\python_work\unit_10\pi_digits.txt"
with open(filename, 'w') as file_object:
    file_object.write ("I love programming.\n")
    file_object.write("I love creating new games.\n")

#10.2.3 添加到文件
filename = 'programming.txt'
with open(filename, 'a') as file_object: 
    file_object.write("I also love finding meaning in large datasets.\n") 
    file_object.write("I love creating apps that can run in a browser.\n")


