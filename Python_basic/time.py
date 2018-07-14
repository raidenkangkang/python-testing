import time

print(time.time())
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print(time.asctime(time.localtime(time.time())))