"""
zip testing,合并后是个list
"""
# 竖向合并，1合并到4，2合并到5，3合并到6
a = [1, 2, 3]
b = [4, 5, 6]
myList = list(zip(a, b))
print(myList)

for i, j in myList:
    print(i * 2, j * 2)

# 位数不一样则会合并基于最短的list
a1 = [1, 2, 3, 7, 11, 22, 33]
b1 = [4, 5]
myList1 = list(zip(a1, b1))
print(myList1)

# zip还可以合并多个元素
myList2 = list(zip(a, a1, b, b1))
print(myList2)
