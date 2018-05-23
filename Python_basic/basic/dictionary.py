#dictiionary is non-order
#first key-value, random sort, not by order
my_keyvalue_dict = {
    "name": "raiden",
    "age": 36,
    "company": "GE",
    "wife": "KK",
    "wife age": 35,
    "kid":{
        "name": "Hong Yu",
        "age": 3.5,
        "sex": "boy"
    }
}

my_keyvalue_dict["new key added"] = "i'm a new key's value" #add a new key & value into the list
for items in my_keyvalue_dict.values(): #show the .value() of each key
    print("values are: {}".format(items))
    
for items in my_keyvalue_dict.keys():
    print("keys are: {}".format(items))

#key check/search
print("this is all the keys: ", my_keyvalue_dict.keys()) #return all the keys in the dict
print("fuck" in my_keyvalue_dict.keys()) #return a faile

#override/update the value
my_keyvalue_dict.update(
        {
            "name":"RAIDEN AGAIN", 
            "wife":"BIG KK"
        })#this will update the values

print(my_keyvalue_dict["age"]) #search value by key
print(my_keyvalue_dict["wife"])

#inner type can also be dictionary
print(my_keyvalue_dict["kid"]["name"]) #nest search
print(my_keyvalue_dict["kid"]["sex"])

#update key value's value
my_keyvalue_dict["kid"]["age"] = 777
print(my_keyvalue_dict["kid"]["age"])

#del function for a specific key
del my_keyvalue_dict["wife"]
print(my_keyvalue_dict)

#delete with pop function
my_keyvalue_dict.pop("wife age") #this is telling the key: wife age, will be removed - both the key and it's value
print(my_keyvalue_dict)

print(my_keyvalue_dict.items()) #list out all items with (key,value) format
for key_info, value_info in my_keyvalue_dict.items():
    print("key: ",key_info," -> value: ",value_info)

#get function, if fuck is in the dict, return value, otherwise return none
print(my_keyvalue_dict.get("name","represent the return value if the key is not exist, default is none"))

#del everything in the dictinoary
my_keyvalue_dict.clear()
print("what's in the new dict: " + str(my_keyvalue_dict)) #shows empty

"""
dictionary testing, 字典是没有顺序的
"""
myStuff = {
    "name":"raiden",
    "age":36,
    "married":True,
    "son/daughter":"son",
    "salary":10000,
    "company":"GE",
    "GE profile": {"sso":"302015572",
                   "email":"raiden.yu@ge.com",
                   "title":"director of cloud"
    }
}

print(myStuff) #字典输出是没有顺序的
print(myStuff["age"]) #字典按照key来搜索
print(myStuff["GE profile"]["email"].upper()) #可以nest嵌套

myStuff["GE profile"]["title"] = "cloud architecture" #更新一个key的value操作
print("after updates on title: {}".format(myStuff["GE profile"]["title"]))

myStuff["phone number"] = "18621650922" #新增一个key/value键值对
print(myStuff)

print("after delete of married key/pair")
del myStuff["married"] #根据key来删除key为married的键值对
print(myStuff)

#循环输出字典内容
for item in myStuff:
    print("key: " + str(item) + " || value: "+ str(myStuff[item])) #循环内容为key