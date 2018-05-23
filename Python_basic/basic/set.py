"""
set是未排序的，唯一的元素组合，功能去掉重复内容, set需要用到set()方法来创建
"""
myList = set()
myList.add(99)
myList.add(99) #set is unique, so this one will not display in the output
myList.add("hello")
# myList.add([1,2,3,4,5]) 无法增加list到set元素里面
# myList.add({"name":"raiden", "age":99}) 也无法增加字典到set元素里面

#set可以去掉重复值,并不会排序
print(myList)

#字符也可以去掉重复,大小写是区分的
myStr = "hhhellooo,,,RRrraidennn 302015572..."
print(set(myStr))

#新增一个内容
newList = set(myStr)
newList.add("new item")
print(newList)

newList.remove("3") #移除一个元素，若元素不存在则会报错
print(newList)

newList.discard("xx not exist but no error") #移除一个元素，若元素不存在则不会报错
print(newList)

#找出newlist里面和myStr不同的内容
print(newList.difference(myStr))

#找出交集(大家都有的元素)
print(newList.intersection(myStr))