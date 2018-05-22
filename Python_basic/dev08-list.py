#list type, start with position 0
user_profile_list = ["raiden", 36, 178]
print(type(user_profile_list))

#full value show
print(user_profile_list) 

#positioning
print(user_profile_list[0])
print(user_profile_list[:1])
print(user_profile_list[:2])

#get all values
for i in user_profile_list:
    print(i)
    
#list append, from the end
user_profile_list.append("kk")
user_profile_list.append(171)
print(user_profile_list)

#update
user_profile_list[0] = "RAIDEN"
print(user_profile_list)

#insert
user_profile_list.insert(1,"GE")
user_profile_list.insert(5,"not GE")
print(user_profile_list)

user_profile_kk = ["KK", "XENCIO"]

#extend a list to existing list as values
user_profile_list.extend(user_profile_kk)
print(user_profile_list)

#append a list into a list
user_profile_list.append(user_profile_kk)
print(user_profile_list)

#remove by value
user_profile_list.remove("kk")
print(user_profile_list)

#pop remove by index
user_profile_list.pop(-1)
print(user_profile_list)

#sort
#user_profile_list.sort(None, False)

#not support for both str and int
#sorted(user_profile_list)