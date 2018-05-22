"""
pickly module testing
用于序列化的两个模块
json：用于字符串和Python数据类型间进行转换
pickle: 用于python特有的类型和python的数据类型间进行转换
json提供四个功能：dumps,dump,loads,load
pickle提供四个功能：dumps,dump,loads,load
"""

import pickle

myFile = open("pickle_file.pickle", "wb")
myDict = {"name":"raiden", "age":36}

#把数据从mydict dump到myfile里面去, 内容只能计算机可以读
pickle.dump(myDict, myFile)
myFile.close()

#用with语句会在工作完成后自动关闭file，无需手工close
with open("pickle_file.pickle", "rb") as newFile:
    myDictNew = pickle.load(newFile)
    
print(myDictNew)