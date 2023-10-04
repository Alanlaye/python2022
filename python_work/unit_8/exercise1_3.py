#8-1 消息
def display_message():
    print("I've learned def in this part.")
display_message()

#8-2 喜欢的图书
def favorite_book(title):
    print("One of my favorite books is "+title.title()+".")
favorite_book('Rain')

#8-3 T-shirt
def make_shirt(size,style):
    print("The size is "+size.title()+".")
    print("The styleis "+style.title()+".")
make_shirt('s','win')
make_shirt(size = 's',style = 'win')

#8-4 大号T-shirt
def make_shirt(size = 'L',style = 'I love Python'):
    print("The size is "+size.title()+".")
    print("The style is "+style.title()+".")
make_shirt()
make_shirt(size = 'm')
make_shirt(style = 'love')


#8-5城市
def describe_city(name = 'paris',country = 'france'):
    print(name.title()+" is in "+country.upper()+".")
describe_city('london','uk')
describe_city('beijing','cn')
describe_city()

#8-6城市名
print('m1')
def city_country(city,country):
    c_c = city.title()+", "+country.title()
    print(c_c)
city_country('apris','france')
city_country('beijing','cn')

print('m2')
def city_country(city,country):
    c_c = city.title()+", "+country.title()
    return c_c
message = city_country('paris','france')
print(message)

#8-7 专辑
def make_album(singer,album,number = ''):
    album_infs = {'singer':singer,'album':album}
    if number:
        album_infs['number'] = number
    return album_infs
album_information = make_album('aa','bb',19)
print(album_information)

#8-8 用户的专辑
def make_album(singer,album):
    album_infs = {'singer':singer,'album':album}
    return album_infs
while True:
    print("\nPlease tell me some infs about your favorite album.")
    print("(enter 'q' at any time to quit)")
    singer = input("singer's name: ")
    if singer == 'q':
        break
    album = input("album's name: ")
    if album == 'q':
        break
    album_information = make_album(singer,album)
    print(album_information)

# 一个拓展：用户的专辑（2）
def make_album(singer,album,number):
    album_infs = {'singer':singer,'album':album}
    if number:
        album_infs['number'] = number
    return album_infs
while True:
    print("\nPlease tell me some infs about your favorite album.")
    print("(enter 'q' at any time to quit)")
    singer = input("singer's name: ")
    if singer == 'q':
        break
    album = input("album's name: ")
    if album == 'q':
        break
    number = input("number: ")
    if number == 'q':
        break
    album_information = make_album(singer,album,number)
    print(album_information)
