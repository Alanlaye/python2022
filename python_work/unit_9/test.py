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
        if check == 'y':
            print("Welcome back, "+username+"!")
        else:
            username = get_new_username()
            print("We'll remember you when you come back, "+username+"!")   
    else:
        username = get_new_username()
        print("We'll remember you when you come back, "+username+"!")

greet_user()