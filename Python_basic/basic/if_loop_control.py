if 10>20:
    print("first block")
elif 10>4: #下面的会跳过，不会被执行
    print("second block")
elif 10>6: #会被跳过，因为上面的elif已经成功了
    print("second.5 block")
else:
    print("third block")
    
#for loops
someSeq = [1,2,3,4,5]
for items in someSeq:
    print(items)


someDict = {"name":"raiden","age":36,"wife":"kk","son":"hongyu"}
#默认是循环字典的key
for items in someDict:
    print("key:{}".format(items) + ", value:{}".format(someDict[items])) #items = key，并不是value

#循环字典的key
for items in someDict.keys():
    print(items)

#循环字典的value
for items in someDict.values():
    print(items)
    
#loop for tuples
myTuples = (1,2,3,4,3,'1')
for items in myTuples:
    print(items)

#while loops
i = 10
while i<15:
    print("i is: {}".format(i))
    i=i+1
    
print(list(range(100,110))) #自动生成一个list, 不包含110
print(list(range(50,70,2))) #自动生成一个list，每2个数字一跳

someNum = range(0,5) #range 产生的list
newNum = [] #empty list

for item in someNum:
    newNum.append(item**3) #3次方数

print(newNum)

newNumTwo = {num+11 for num in someNum} #和for语句一样，简化语句,转成set
print(newNumTwo)

i=0
while True and i<10: #while true 永远执行除非不是true了
    print ("I'm true")
    i=i+1
    
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
        break #if i==7, this will quit the entire remaining loop, no more 7, 8, 9, 10 execution
    print("break testing: " + str(i))
    
#pass testing
for i in range(5):
    pass #nothing will happen after this line, it's a placeholder only
    print("will this get printed ?") #this will get printed
    
#combination testing
x = 0
for i in range(6): # 0,1,2,3,4,5 values
    print("i: " + str(i))
    x = x + i
print(x)