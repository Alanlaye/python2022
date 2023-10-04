###7.1

#7-1 汽车租赁
message = input('What kind of car do you wnat? ')
print('Let me see if I can find you a '+message+'!')

#7-2 餐馆订位
prompt = 'How many guests are there?'
people = input(prompt )
if int(people) > 8:
    print('Sorry!We have no extra tables!')
else:
    print('Got it!')

#7-3 10的整数倍
number = input("Enter a number and I'll tell you whether it is 10 beishu: ")
if int(number) == 0:
    print("Yes,it is.")
else:
    print("No,it,isn't.")


