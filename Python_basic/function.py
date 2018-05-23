'''
define your own function
'''

import random #library for generate random number

#global parameter, can be accessed within the function definiation
global BIG_NUMBER
global USD_RATE #全局变量，通常大写
BIG_NUMBER = 0
USD_RATE = 6.54

#first function
def my_cal (left_number, right_number):
    """
    to add the two numbers together, and this is a docstring for this function
    """
    return left_number + right_number

#random module, randint function
x = random.randint(1,30)
y = random.randint(1,30)

print(my_cal(x,y))

#get help function
#help(my_cal) get help descirption of the function
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

#put *in front of argu will take the all extra arg, like below, x="default" means if no input from the code, then take this as a default value.
def my_funct3(x="default is raiden", y="default is kk", *ext_arg):
    print(x+"-----"+y)
    return
#if only give one value, the others will take from funct def default values
my_funct3("I'm not default")

#测试1
def strEndCheck (strA, strB):
    a = strA.lower()
    b = strB.upper()
    return a.endswith(b)
    
testResult = strEndCheck(strA="ok",strB="k") #可以强调每个参数是什么值
print(testResult)

#测试2
def doubleChar(someString):
    result = ''
    for char in someString:
        result = result + char * 2
    return result
    
print(doubleChar(someString="raiden"))

def sellCarFunc(carBrand, isSecondHand, carPrice, carCountry="China", carColor="black"): #默认值的参数后面的参数也必须是有默认值的，否则报错，只能把没有默认值的参数全部放到前面，有默认值的放到后面
    """
    print函数可以多行执行
    """
    print(
        "car brand:", carBrand,
        "second y/n:", isSecondHand,
        "price: ", carPrice,
        "color: ", carColor,
        "country: ", carCountry
        )

sellCarFunc("BMW", "yes", 55000/USD_RATE, "US", "red")
print(USD_RATE)