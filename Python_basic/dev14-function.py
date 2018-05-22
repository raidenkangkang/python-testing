'''
define your own function
'''

import random

#global parameter, can be accessed within the function definiation
global big_number
big_number = 0

#raiden first function
def my_cal (left_number, right_number):
    #add function
    return left_number + right_number

#random module, randint function
x = random.randint(1,500)
y = random.randint(1,500)

print(my_cal(x,y))

#get help function
#help(random.choice)
#help(random.randint)

def my_list_calculation (some_list):
    #determin the type of list
    #return a random choice of the input list
    if str(type(some_list)) == "<class 'list'>":
        return random.choice(some_list)                 
    #if not list, then return error string
    else:
        return "Only support list parameter !"
        #after return, nothing will get executed
    
my_list = [-1,0,1,4,6,8,6,45]
print(my_list_calculation(my_list))
print(my_list_calculation("hello function"))
#print(str(type(my_list)))
#help(random)


#define parameters in function itself, parameter inside=function parameter, only works inside the parameter
def my_funct2 ():
    big_number = 101
    print(big_number)
    return

my_funct2()
print(big_number)


#put *in front of argu will take the all extra arg, like below
def my_funct3(x="default is raiden", y="default is kk", *ext_arg):
    print(x+"-----"+y)
    return
#if only give one value, the others will take from funct def default values
my_funct3("I'm not default")

my_new_dict = {
    "name1":"raiden",
    "name2":"KK"
}

#convert list or dict into the function
my_funct3(my_new_dict["name1"],my_new_dict["name2"])
my_funct3(str(my_list[1]),str(my_list[2]),"kkk","more than 3","more then 4 input")