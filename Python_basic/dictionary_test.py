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
