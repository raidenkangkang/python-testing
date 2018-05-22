str_one = "hello"
str_two = "hello world"

#determine if somestring is in somestring
print(str_one in str_two) #true
print("f" in str_two) #false
print("A" not in str_two) #true
print(str_one != str_two) #true

'''
string array
positive: start from 0 as first one
negative: start from -1 as first one
''' 
print(str_one[3])
print(str_one[-1])

#from 0 - first position, up to 5th character
print(str_two[2:5])

#from first, to 6 char
print(str_two[:9])

#from 8th char to the end of the string
print(str_two[8:])
print(str_two[-5:])

#get char string every 2 position
print(str_two[::2])

#%d = number, %s = string, pass as parameter, but this one seems not working !!!!!
str_three = "I have %d apples in %s"
str_three % (5, "home")
print(str_three)