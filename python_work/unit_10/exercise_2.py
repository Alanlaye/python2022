#10-3 访客
filename = r"C:\Users\零落\Desktop\python_work\unit_10\guest.txt"
with open(filename,'a') as file_object:
    name = input("Please write down your name here: ")
    file_object.write(name)

#10-4 访客名单
while True:
    message = "Enter your name here: "
    message += "Enter 'quit' when you finish."
    guest = input(message)
    if guest == 'quit':
        break
    else:
        print("Hello, "+guest.title())
        filename = r"C:\Users\零落\Desktop\python_work\unit_10\guest_book.txt"
        with open(filename,'a') as file_object:
            file_object.write(guest+'\n')
#my method
#answer method
#区别在于文件打开和关闭的次数 确实filename应该放在最前边
#循环完再关掉（只用打开和关闭一次）

filename = r"C:\Users\零落\Desktop\python_work\unit_10\guest_book.txt"
print("Enter 'quit' when you finish.")
while True:
    name = input("\nWhat's your name? ")
    if name == 'quit':
        break
    else:
        with open(filename,'a') as f:
            f.write('\n'+name+'\n')
            print("Hello, "+name.title())

#10-5 关于编程的调查
filename = r"C:\Users\零落\Desktop\python_work\unit_10\reason.txt"
print("Enter'quit' when you finish." )
while True:
    reason = input("why you like programming? ")
    if reason == 'quit':
        break
    else:
        with open(filename,'a') as f:
            f.write(reason+'\n')


