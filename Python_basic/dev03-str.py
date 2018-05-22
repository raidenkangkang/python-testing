'''
string testing
'''

str_one = "hello man"
print(type(str_one))

#\n = enter
str_two = "hello girl \n kk"
print(str_two)

#\'' means nothing
str_three = "hello \'Mary"
print(str_three)

#\t is space
str_four = "hello number \t\t4th"
print(str_four)

#r in front of string means original string
str_five = r"hello \t\n\' number5"
print(str_five)

print(str_three + str_four)

#convert 
x = 123
y = str(x)
print(type(y))