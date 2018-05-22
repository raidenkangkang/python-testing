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