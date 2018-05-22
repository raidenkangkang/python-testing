"""
map testing
"""

def addFunc(x,y):
    return x+y

#map可以把多个值传入function的参数,若值不匹配则取少的满足条件的,以下case没有map需要调用多次function，但是参数位数要一样，比如2个参数不能放3个
myList = list(map(addFunc,[1,2,3],[4,5,6,10]))
print(myList)

myList2 = list(map(lambda x:x**2, [1,2,3,4,5,6,7]))
print(myList2)