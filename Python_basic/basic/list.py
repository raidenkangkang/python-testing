#list type, start with position 0
user_profile_list = ["raiden", 36, 178]
print(type(user_profile_list)) #type is <class 'list'>
print(user_profile_list)  #show all the values of the list

#positioning
print(user_profile_list[0])
print(user_profile_list[:1]) #same as string
print(user_profile_list[:2])

#get all values
for i in user_profile_list: #for loop to get everything
    print(i)
    
#list append, from the end
user_profile_list.append("kk") #add a new value at the end
user_profile_list.append(171)
print(user_profile_list)

#update
user_profile_list[0] = "RAIDEN" # list can do update
print(user_profile_list)

#insert
user_profile_list.insert(1,"GE") #insert into a specific position of the value
user_profile_list.insert(5,"not GE")
print(user_profile_list)

print("new line starts here.......")
user_profile_kk = ["KK", "XENCIO"]
user_profile_list.extend(user_profile_kk) #extend a list's all value to an existing list, basically add the value to the list
print(user_profile_list)

user_profile_list.append(user_profile_kk) #append a list into a list (as a list item inside a list)
print(user_profile_list)
print("new line starts here.......\n")

user_profile_list.remove("kk") #remove by value
print(user_profile_list)

user_profile_list.pop(-1) #pop remove by index, remove the last object in the list
user_profile_list.pop(2) #remove index 2 object in the list
print(user_profile_list)

myList1 = [101,22,33,411.00,50.987] #数字型list
myList2 = ["hello","raiden","kk","hongyu","raiden"] #字符型list
myList3 = ["raiden",35,"KK",34,"hongyu",3.59,True] #混合型list
myList4 = [["name","raiden"],["name","kk"],["name","hongyu"],36.3,35.4,3.98,"GE","Xencio"] #list里面嵌套list
print(myList1)
print(len(myList1)) #给出一共几个值

print("count of raiden is: " + str(myList2.count("raiden")))  #count是统计raiden出现个次数
print("before updates: {}".format(myList3)) #list是mutable类型的，可以增加，删除和更新
myList3[0] = "RAIDEN"
print("after updates: {list3}".format(list3=myList3))
myList3.append("added into as last value") #append在list最后增加
print("after append: {list3}".format(list3=myList3))
myList3.insert(2,"inserted item") #insert 操作，第一个2表明0，1，2位置后插入
print("after insert: {list3}".format(list3=myList3))
myList3.extend(myList2) #extend 会extend两个list合并为一个，和append不同
print("after extend: {list3}".format(list3=myList3))
print(myList4)
print("after pop(): {list4}, item removed = {removedItem}".format(list4=myList4,removedItem=myList4.pop())) #pop是删除list的最后一个值,而且pop会返回remove的那个值
myList4.remove(36.3) #删除第一个为36.3的list值
print("after remove of 36.3: {}".format(myList4))
myList4.reverse() #reverse会反转顺序
print("after reverse: {}".format(myList4))
print("nest search: {}".format(myList4[4][1])) #nest查询，查找返回的list里面的一个值，可以多个嵌套
print("index search of GE at position of: " + str(myList4.index("GE"))) #根据值来搜索返回该第一个值出现的位置，若值不存在则报错
print("before sorting: {}".format(myList1))
myList1.sort() #从小到大排序, 而且不可以和string混合，默认是从小到大，只能是数字
print("after sorting: {}".format(myList1))
myList1.sort(reverse=True) #从大到小排序，reverse=true
print("after reverse sorting: {}".format(myList1))

#for 循环输出list内容
print("another line for below: " + str(len(myList4)))
for index in range(len(myList4)):
    print("index: {}".format(str(index)) + ", value:" + str(myList4[index]))
    
oneDimList = [1,2,3] #一维list

twoDimList = [ #二维list
        [1,2,3],
        [2,3,4],
        [5,6,7],
        [9,9,10]
    ]

oneDimList.append(["ok","okok"]) #append add the list into the list, if the item is a list, extend will just insert the value
print(oneDimList)

oneDimList.extend(["not ok", "not okok", 99, "not ok"])
print(oneDimList)