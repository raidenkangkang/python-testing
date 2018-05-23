"""
lambda testing
"""
def myFunc(x):
    print(x+1)
myFunc(12)
#上面函数等于以下lambda函数，左边的x是输入，右边的是输出
myResult = lambda x: x+1
print(myResult(12))

#输入是x，y，输出是x+y如果x可以整除2,否则输出Goodbye
calResult = lambda x,y: x+y if x%2==0 and y%2==0 else "goodbye"
print(calResult(10,4))
print(calResult(9,5))

#输入的x，输出固定就是 juxt X字符
strResult = lambda x: "just X"
print(strResult("y"))

#lambda与for循环
f = [lambda x: x*i for i in range(4)]
print(f[1](3))