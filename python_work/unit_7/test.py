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
