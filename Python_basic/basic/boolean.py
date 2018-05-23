'''
if-else, true and false
'''

#
user_input = input("input your name...")
user_input_age = input("input your age...")

#if, else
if user_input == "raiden":
    print("ok you are raiden")
elif user_input == "100":
    print("ok you are number")
elif not user_input:
    print("nothing input...")
else:
    print("ok, input something but not pre-defined...")
    
    
#name and age check...
if str(user_input).__len__() >= 5 and int(user_input_age) >= 18:
    print("length check: STATUS OK")
    print("age check: STATUS ok")
elif str(user_input).__len__() >= 5 and int(user_input_age) < 18:
    print("length check: STATUS OK")
    print("age check: FAILED")
elif not user_input:
    user_input = input("please put your name here....")
else:
    print("validation failed...")
    
    
print(True) #true
print(False) #false
print(True & False) #false
print(True & True) #true
print(False & False) #false
print(True or True) #true
print(True or False) #true
print(False or False) #false

myTuple = (1,2,3,4,5,"raiden",36.56,["first name","last name"]) #tuple是不可更改的,immutable类型，和string一样，也支持混合数据类型
print(myTuple[7])
print(myTuple[-2])

# myTuple[0] = 13 'tuple' object does not support item assignment,不可赋值更新


#set是unorder的，unique的
mySet = set({1,2,4,4,4,4,4,55,"company",36,"302015572",36, ("name","home address","phone number")})
mySet.add(9999)
print(mySet)