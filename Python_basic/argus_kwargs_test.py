"""
*args and **kwargs testing
"""

#添加无限数量的参数
def unlimitedArgus (firstArgs, *unlimited):  # *后面的会转换为一个()，无需作为key value形式传入
    print(firstArgs)
    print(unlimited)
    return sum(unlimited)
    
print(unlimitedArgus("1",2,3,4,5,6,7,8))



def unlimitedKwargs (**unlimitedKwargs): #Kwargs返回一个字典, 需要以key value形式传入数据
    print(unlimitedKwargs)
    
unlimitedKwargs(name="raiden", school="GE", sso="302015572", son="hongyu", wife="kk")

#混合args和kwargs
def mix(*args, **kwargs):
    print(args)
    print(kwargs)
    
mix(1,2,3,4,11231235,name="son",car="infiniti")