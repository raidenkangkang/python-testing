"""
function testing
"""


def myFirstFunc(parameter="default input"):
    """
    this is the function docstring description, 鼠标选中这个function会有说明显示
    """
    
    print("my first function: {}".format(parameter))
    
myFirstFunc()


def mySecondFunc():
    """
    this is just return some string
    """
    return "hello world !"
    
strReturn = mySecondFunc()
print(strReturn)


def addFunc(num1, num2):
    """
    2个数字加法但是会检查类型
    """
    if type(num1) == type(num2) == type(10): #检查int类型是否一致
        return num1+num2
    else:
        return "wrong arg type, can't do add function"

print(addFunc(1,4.3))



#lambda, 只可能用一次，无需定义功能
myList = range(0,20)
    
evenNum = filter(lambda someInput:someInput>=10 and someInput%2==0, myList)
"""
someNum: 程序输入
:之后的是满足计算条件后的return内容
"""
print(list(evenNum))


#测试1
def strEndCheck (strA, strB):
    a = strA.lower()
    b = strB.lower()
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


USD_RATE = 6.54 #全局变量，通常大写

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