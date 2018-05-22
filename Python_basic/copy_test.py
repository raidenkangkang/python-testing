"""
copy test
"""

import copy #copy是一个模块

a = [1,2,3]
b = a  #内存索引和a一样
c = copy.copy(a) #内容一样，内存地址不一样, shadow copy, 但是第二层开始的内存一样，除非用deepcopy

print(a,b,c)

print(id(a))
print(id(b))
print(id(c)) #和上面的ab不一样


d = copy.deepcopy(a) #对象和子对象都不会重复
print(id(d))
