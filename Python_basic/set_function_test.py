"""
set功能去掉重复内容
"""

myList = [1,2,1,1,1,2,2,2,3,4,5,6]

#set可以去掉重复值,并不会排序
print(set(myList))

#字符也可以去掉重复,大小写是区分的
myStr = "hhhellooo,,,RRrraidennn 302015572..."
print(set(myStr))

#新增一个内容
newList = set(myStr)
newList.add("new item")
print(newList)

#移除一个元素，若元素不存在则会报错
newList.remove("o")
print(newList)

#移除一个元素，若元素不存在则不会报错
newList.discard("xx not exist but no error")
print(newList)

#找出newlist里面和myStr不同的内容
print(newList.difference(myStr))

#找出交集(大家都有的元素)
print(newList.intersection(myStr))