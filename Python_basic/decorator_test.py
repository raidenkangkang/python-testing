"""
修饰器语法糖测试, a function called before another function is called，就是增强现有的function
"""

def myDecorator(someFunctionToRun):
    def runTheActualFunction(): #这个函数将代替传入的函数
        print("before decorator runs")
        someFunctionToRun() #此处运行传入的函数功能，其实就是下面的myFunction
        print("after decorator runs")
    return runTheActualFunction
    
    
#其解释器会解释成下面这样的语句：func = decorator(func)
#多个装饰器调用func = decorator_one(decorator_two(func))
#带参数的decorator：func = decorator(arg1,arg2)(func)
@myDecorator #会把myFunction 传入这个decorator后去执，然后执行这个myFunction
def myFunction():
    print("I am the actual function")
    
myFunction()


#下面的代码和上面的一样，只是外层再增加一个function来传递参数
def myTopDecorator(someDecoratorArgus):
    def myDecorator(someFunctionToRun):
        def runTheActualFunction(*args, **kwargs): #这个函数将代替传入的函数, 确保带有*args and **kwargs因为被修饰的函数可能带有参数
            print(someDecoratorArgus + " - before decorator runs")
            if someDecoratorArgus == "run":
                someFunctionToRun(*args, **kwargs) #此处运行传入的函数功能，其实就是下面的myFunction, 确保带有*args and **kwargs
            else:
                print("not run the function")
            print(someDecoratorArgus + " - after decorator runs")
        return runTheActualFunction
    return myDecorator #由于额外增加了一层， 所以需要返回
    
#带参数的decorator：func = decorator(arg1,arg2)(func)
@myTopDecorator("run") #会把myFunction 传入这个decorator后去执，然后执行这个myFunction
def myFunctionTwo(x, y):  #带有参数
    print(x+y)
    
myFunctionTwo(100,12)