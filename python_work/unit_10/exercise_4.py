#10-11,10-12 喜欢的数字
import json
filename = 'remember_favorite_number.json'

def get_stored_number():
    try:
        with open(filename,'r') as f:
            number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return number
    
def get_new_number():
    number = input("Enter your favorite number: ")
    with open(filename,'w') as f:
        json.dump(number,f)
    return number



def show_favorite_number():
    number = get_stored_number()
    if number:
        print("I know your favorite number! It's "+str(number)+" !")
    else:
        number = get_new_number()
        #在这里需要加一个number = 再更新一次变量
        print("I will remember your favorite number:"+str(number)+"!")

show_favorite_number()