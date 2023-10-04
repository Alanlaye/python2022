#7-4 披萨配料
print("M1")
prompt = "Please write down the pizza you want: "
prompt+= "Enter 'quit' when you have finished."
toppings = ""
while toppings != 'quit':
    toppings = input(prompt) 
    print("We've added "+toppings+"!")
#如果只是单纯打印toppings可以通过调换顺序，但是放在句子中就行不通
#好吧 不调换顺序的代码也会多输出一行 不加if测试或者false测试就不行   

print("M2")
prompt = "Please write down the pizza you want: "
prompt+= "Enter 'quit' when you have finished."
toppings = ""
while toppings != 'quit':
    toppings = input(prompt)
    if toppings != 'quit':
        print("We've added "+toppings+"!")
#变量active
print('M3')
prompt = "Please write down the pizza you want: "
prompt+= "Enter 'quit' when you have finished."
active = True
while active:
    toppings = input(prompt)
    if toppings == 'quit':
        active = False
    else:
        print("We've added "+toppings+"!")

#break语句
print('M4')
prompt = "Please write down the pizza you want: "
prompt+= "Enter 'quit' when you have finished."
while True:
    toppings = input(prompt)
    if toppings == 'quit':
        break
    else:
        print("We've added "+toppings+"!")

