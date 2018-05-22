print(2**10) #2的10次方
print(4**0.5) #4的开根号
print(9%2) #运算结果的余数=1
print(8%2) #运算结果的余数=0
print(8%3) #运算结果的余数=2

print(9//3) #多少个3得到9， =3
print(8//3) #多少个3得到8， =2
print(15//7) #多少个7得到15， =2

myIncome = 50000
myTax = 0.25
myRevenue = myIncome * myTax
print(myRevenue)

print("i'm raiden") #可以把单引号放入双引号

myName = "i'm raiden. RAIDEN is my english name"
print(myName[5]) #从0开始
print(myName[-2]) #负号从尾部开始
print('I\'m apple') #\'表示把后面的分号当成字符
print(myName[10:]) #python slicing, 从第10位开始到最后
print(myName[:7]) #python slicing, 从第一位开始到第6位,一共7个，从0开始，但是不包含7
print(myName[5:10]) #python slicing, 从第5位开始到第10位字符
print(myName[:]) #python slicing, 从头开始到结束
print(myName[::1]) #python slicing, 从头开始，每一位显示
print(myName[::-1]) #python slicing, 从最后开始往前显示，reverse显示
print(myName[::3]) #python slicing, 从头开始，每（第）三位显示
#myName[9] = "ok" 会报错，string是immutable类型，不可赋值
print(myName.upper()) #全部大写
print(myName.lower()) #全部小写
print(myName.capitalize()) #每一段的第一个字符是大写的
print(myName.split()) #按照每个词语分割成数组
print(myName.split("na")) #按照na来分割，na将在输出中被去掉
print("hello there: {y} and hello again {x}, final hello: {z}".format(x=myName, y="this is hello from KK", z="hongyu hello !")) #format里面的string会被instert到{}中,可以通过{x}里面放置变量来做mapping

print("number converted to string now: " + str(12.30)) #转换成字符串
print(int("56")+990.12) #string转换成整数
print(float("99.123")+100.76) #string转换成float小数


a, b, c, d = 100, 200, 300, "hello" #可以一次定义多个变量和赋值
print(a, b, c, d) #可以一次打印多个变量