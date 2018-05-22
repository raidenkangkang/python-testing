"""
把function作为函数传递
"""

def addFunc():
    return 1+3
    
def mainFunc(anotherFunc):
    return anotherFunc()
    
x = mainFunc(addFunc) #方法作为参数传递进来后不要放（）括号
print(x)
    
    
