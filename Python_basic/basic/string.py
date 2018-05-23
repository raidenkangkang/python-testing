'''
string method testing
'''

str_one = "hello raiden"
print(str_one.upper()) #upper case
print(str_one.count("l")) #do a count of character X

#split by character
str_two = "192.168.12.10"
print(str_two.split("."))
print("new line from here.........")
print(str_one.join(str_two)) #string join
print(str_two.find("10"))

str_one = "hello"
str_two = "hello world"
print("new line from here.........")
print(str_one in str_two) #true, #determine if somestring is in somestring
print("f" in str_two) #false
print("A" not in str_two) #true
print(str_one != str_two) #true

'''
string array
positive: start from 0 from first one
negative: start from -1 from last one
''' 
print("new line from here.........")
print(str_one[1]) # = e
print(str_one[-1]) # = o
print(str_two[2:4]) # from position 2 to position 3 (not count 4th)
print(str_two[:9]) #from first, to 8th char
print(str_two[8:]) #from 8th char to the end of the string
print(str_two[-5:]) #from last 5th to the end of the string
print(str_two[::2]) #get char string every 2 position


str_one = "hello man"
print(type(str_one)) #return the type the object

str_two = "hello girl \nkk" #\n = enter into a new line
print(str_two)

str_three = "hello \'Mary\'" #\'means '
print(str_three)

str_four = "hello number \twith a tab space" #\t is tab space
print(str_four)

str_five = r"hello \t\n\' number5"#r in front of string means original string, it will ignore the \t and \n
print(str_five)

print("string with some input of {Y}, and {X}".format(X="---I am X---", Y="---I am Y---")) #parameter way to join the string with .format function


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