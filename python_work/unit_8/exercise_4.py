#8-9 魔术师
def show_magicians(magicians):
    for magician in magicians:
      print(magician)
magicians = ['aa','bb','cc']
show_magicians(magicians)
#8-10 了不起的魔术师
def make_great(magicians,great_magicians):
   while magicians:
      making_great_magicians = "The Great "+magicians.pop()
      great_magicians.append(making_great_magicians)
magicians = ['aa','bb','cc']
great_magicians = []
make_great(magicians,great_magicians)
show_magicians(great_magicians)


#8-10 了不起的魔术师
def make_great(magicians,great_magicians):
   while magicians:
      making_great_magicians = "The Great "+magicians.pop()
      great_magicians.append(making_great_magicians)
magicians = ['aa','bb','cc']
great_magicians = []
make_great(magicians[:],great_magicians)
show_magicians(great_magicians)
show_magicians(magicians)