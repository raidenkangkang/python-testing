'''
for xxx in xxx
 if abc
    xxx
'''

#for loop testing
for i in range(20):
    print(i)
    if i >= 15:
        print("ok now higher then 10: " + str(i))

#continue testing...
for i in range(10):
    if i==3:
        print("i==3, so will not print 3")
        continue ##this will skip the rest code if i == 3
    print(str(i))
    
    
#break testing
for i in range(10):
    if i==7:
        break #if i==7, this will quit the current loop, no more 7, 8, 9, 10 execution
    print("break tseting: " + str(i))
'''    
#while testing
while 1: ##this will be an endless loop
    a = input("input something...")
    if a == "break":
        break #if input is raiden, then will exit current loop
'''
    
#pass testing
for i in range(5):
    pass #nothing will happen, it's a placeholder
    print("will this get printed ?") #this will get printed
    

#combination testing
for i in range(10):
    print("new num:" + str(i))
    if i==3:
        a=input("let's have a break:")
        if a=="cool":
            break
        
#combination testing
x = 0
for i in range(6): # 1-5 values
    print("i: " + str(i))
    x = x + i
print(x)