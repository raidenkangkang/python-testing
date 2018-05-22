'''
File IO operation in Python
'''

#import the model
import os

'''
r - read
w - write
a - write in the end of the file, if file not exist then create
+ - update the file
b - open file in byte
u - support all \r \n \r\n
'''

#open the file
my_file = open("github/raiden-py-dev/README.md","r")
print(my_file)
