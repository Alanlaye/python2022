from collections import OrderedDict 
favorite_languages = OrderedDict() 
#创建了OrderedDict类的一个实例(一个空的有序字典)
#并将其存储到favorite_languages中
favorite_languages['jen'] = 'python' 
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'
for name, language in favorite_languages.items(): 
    print(name.title()+"'s favorite language is "+
        language.title()+".")
#将以添加的顺序获取调查结果



