"""
list testing
"""

myList1 = [101,22,33,411.00,50.987] #数字型list
myList2 = ["hello","raiden","kk","hongyu","raiden"] #字符型list
myList3 = ["raiden",35,"KK",34,"hongyu",3.59,True] #混合型list
myList4 = [["name","raiden"],["name","kk"],["name","hongyu"],36.3,35.4,3.98,"GE","Xencio"] #list里面嵌套list


print(myList1)
print(len(myList1)) #给出一共几个值


print(myList2)
print(myList2[1]) #打印出第二位值
print(myList2[-2]) #打印倒数第二位的值
print(myList2[1:]) #打印从第二位开始到最后
print(myList2[:2]) #从头开始打印2个值

print("count of raiden is: " + str(myList2.count("raiden")))  #count是统计raiden出现个次数


#list是mutable类型的，可以增加，删除和更新
print("before updates: {}".format(myList3))
myList3[0] = "RAIDEN"
print("after updates: {list3}".format(list3=myList3))


myList3.append("added into as last value") #append在list最后增加
print("after append: {list3}".format(list3=myList3))


myList3.insert(2,"inserted item") #insert 操作，第一个2表明0，1，2位置后插入
print("after insert: {list3}".format(list3=myList3))


myList3.extend(myList2) #extend 会extend两个list为一个，和append不同
print("after extend: {list3}".format(list3=myList3))


print(myList4)
print("after pop(): {list4}, item removed = {removedItem}".format(list4=myList4,removedItem=myList4.pop())) #pop是删除list的最后一个值,而且pop会返回remove的那个值


myList4.remove(36.3) #删除第一个值为36.3的值
print("after remove of 36.3: {}".format(myList4))


myList4.reverse() #reverse会反转顺序
print("after reverse: {}".format(myList4))


print("nest search: {}".format(myList4[4][1])) #nest查询，查找返回的list里面的一个值，可以多个嵌套
print("index search of GE at position of: " + str(myList4.index("GE"))) #根据值来搜索返回该第一个值出现的位置，若值不存在则报错


print("before sorting: {}".format(myList1))
myList1.sort() #从小到大排序, 而且不可以和string混合，默认是从小到大
print("after sorting: {}".format(myList1))
myList1.sort(reverse=True) #从大到小排序，reverse=true
print("after reverse sorting: {}".format(myList1))


#for 循环输出list内容
print("another line for below: " + str(len(myList4)))
for index in range(len(myList4)):
    print("index: {}".format(str(index)) + ", value:" + str(myList4[index]))
    
    
#一维list
oneDimList = [1,2,3]

#二维list
twoDimList = [
        [1,2,3],
        [2,3,4],
        [5,6,7],
        [9,9,10]
    ]