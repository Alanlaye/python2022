#7-8熟食店
sandwich_oders = ['aa','bb','cc']
finished_sandwich = []
while sandwich_oders:
    mading = sandwich_oders.pop()
    print("I made your "+mading)
    finished_sandwich.append(mading)
print('\nThe following sandwiches have been finished.')
for sandwich in finished_sandwich:
    print(sandwich)

#7-9 
sandwich_oders =['aa','bb','cc','cc','cc']
print('cc is out of use.')
while 'cc' in sandwich_oders:
    sandwich_oders.remove('cc')
print(sandwich_oders)

sandwich_oders =['aa','bb','cc','cc','cc']
for sandwich in sandwich_oders:
    sandwich_oders.remove('cc')
print(sandwich_oders)

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
while 'cat' in pets:
    pets.remove('cat')
print(pets)

pets = ['dog','cat','rabbit','cat','lion','cat']
for pet in pets:
    pets.remove('cat')
print(pets)

##有一个问题 while的remove和 for的remove有什么区别（？）
##貌似没区别

#7-10 梦想的度假胜地
dreaming_visits = {}
active = True
while active:
    name = input("what's your name? ")
    place = input("Where would you like to go? ")
    dreaming_visits[name] = place
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        active = False
print("\n--- Poll Results ---")
for name,place in dreaming_visits.items():
    print(name+" would like to go to "+place+".")