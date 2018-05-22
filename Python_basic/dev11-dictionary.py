'''
dictionary type, {im dict}, the key-value !!!
'''

#first key-value, random sort, not by order
my_keyvalue_dict = {
    "name":"raiden",
    "age":36,
    "company":"GE",
    "wife":"KK",
    "wife age":35,
    "kid":{
        "name":"Hong Yu",
        "age":3.5,
        "sex":"boy"
    }
}

#add a key & value into the list
my_keyvalue_dict["new key added"] = "i'm a new key's value"

#key check/search
print("this is all the keys: ", my_keyvalue_dict.keys()) #return all the keys in the dict
print("fuck" in my_keyvalue_dict.keys()) #return a faile

#override/update the value
my_keyvalue_dict.update(
        {
            "name":"RAIDEN AGAIN", 
            "wife":"BIG KK"
        })#this will update the values

print(my_keyvalue_dict)
print(my_keyvalue_dict["age"])
print(my_keyvalue_dict["wife"])
print(my_keyvalue_dict["kid"])

#inner type can also be dictionary
print(my_keyvalue_dict["kid"]["name"])
print(my_keyvalue_dict["kid"]["sex"])

#update key value's value
my_keyvalue_dict["kid"]["age"] = 3.7
print(my_keyvalue_dict["kid"]["age"])

#del function for a specific key
del my_keyvalue_dict["wife"]
print(my_keyvalue_dict)

#delete with pop function
my_keyvalue_dict.pop('wife age') #this is telling the key: wife age, will be removed - both the key and it's value
print(my_keyvalue_dict)

#list out all items with (key,value) format
print(my_keyvalue_dict.items())
for key_info, value_info in my_keyvalue_dict.items():
    print("key: ",key_info,"-------------value: ",value_info)

#get function, if fuck is in the dict, return value, otherwise return none
print(my_keyvalue_dict.get("baby","here represent the return value if the key is not exist, default is none"))


#del everything in the dictinoary
my_keyvalue_dict.clear()
print("what's in the new dict: " + str(my_keyvalue_dict)) #shows empty

'''
#del the entire dic object
del my_keyvalue_dict
print("object level delete: " + str(my_keyvalue_dict))
can't run this as the object is entirely deleted from the memory, NameError: name 'my_keyvalue_dict' is not defined
'''