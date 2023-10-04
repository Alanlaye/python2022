#coding=gbk

#3-4 嘉宾名单
members=['Yaminy','Alan','Laye']
print(members)

#3-5 修改名单
members=['Yaminy','Alan','Laye']
print(members[-1])
members[-1]='Monica'
print(members)
message='Welcome to my wedding ceremony!，'+members[-1]+'!'
print(message)
message='Welcome to my wedding ceremony!，'+members[0]+'!'
print(message)
message='Welcome to my wedding ceremony!，'+members[1]+'!'
print(message)

#添加嘉宾
print("I've found a larger table which can contain more guests,so I can invite more friends.")
members=['Yaminy','Alan','Laye']
members.append('Alex')
members.insert(1,'Hermos')
members.insert(0,'Achiliss')
print(members)
message='Welcome to my wedding ceremony!，'+members[0]+'!'
print(message)
message='Welcome to my wedding ceremony!，'+members[1]+'!'
print(message)
message='Welcome to my wedding ceremony!，'+members[2]+'!'
print(message)
message='Welcome to my wedding ceremony!，'+members[3]+'!'
print(message)
message='Welcome to my wedding ceremony!，'+members[4]+'!'
print(message)
message='Welcome to my wedding ceremony!，'+members[5]+'!'
print(message)

#缩减名单
print("The table I bought can't arrive timely, so I can only invite two guests now.")
popped_members=members.pop(0)
message="Dear "+popped_members+",I'm so sorry to tell you that the invitation has been declined now."
print(message)

popped_members=members.pop(0)
message="Dear "+popped_members+",I'm so sorry to tell you that the invitation has been declined now."
print(message)

popped_members=members.pop(0)
message="Dear "+popped_members+",I'm so sorry to tell you that the invitation has been declined now."
print(message)

popped_members=members.pop(0)
message="Dear "+popped_members+",I'm so sorry to tell you that the invitation has been declined now."
print(message)

print(members)
message="Dear "+members[0]+",you're still welcomed to my wedding ceromony!"
print("\n")
print(message)
message="Dear "+members[1]+",you're still welcomed to my wedding ceromony!"
print(message)

print("\n")
del(members[0])
print(members)
del(members[0])
print(members)



