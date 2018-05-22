"""
错误处理
"""
#try 语句的执行，如果有异常则调用except语句内容，若没有异常则调用else语句内容
try:
    myFile = open("not_exist_file.txt", "r") #文件不存在，会抛出异常
    
#有异常就用Exception里面语句,就不会执行else里面语句了
except Exception as error:  
    print("file I/O error: " + str(error))
    userResponse = input("do you need to create the file ? >")
    if userResponse == "y":
        myFile = open("not_exist_file.txt", "w")
        myFile.write("new file created !")
    else:
        pass
    
#try没有错误就调用else里面的语句
else:
    myContent = myFile.readlines()
    print(myContent)
    myFile.close()