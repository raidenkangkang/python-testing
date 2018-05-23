#import os module for IO operation
import os

for i in range(10):
    #check if the file already exist
    if os.path.isfile("github/raiden-py-dev/login.log"):
        print("already locked !")
        break
    else:
        user_name = input("login: ")
        user_pwd = input("code: ")
        if user_name == "raiden" and user_pwd == "ok":
            print("welcome")
            break
        elif i == 2:
            print("locked !", i+1)
            open("github/raiden-py-dev/login.log","w").write("lock again in the file")
            break
        else:
            pass