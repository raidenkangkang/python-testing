"""
contine和break的测试
"""
#break 测试
while True:
    a = input("type something (if its kk then quit): ")
    if a == "kk":
        break #break来跳出整个循环
    else:
        pass
    
#continue 测试
for x in range(20):
    if x%2 != 0: #1,3,5,7,9等数值
        continue #contine会跳过下面的语句然后从新开始循环
    else:
        print("num: " + str(x))