"""
正则表达式测试
"""

import re #regular expression模块

#普通匹配，不用正则表达式
myStr1 = "dog"
myStr2 = "cat"
testStr = "DOG eat cats and cat"
print(myStr1 in testStr)
print(myStr2 in testStr)

#简单正则表达式的查找
print(re.search(myStr1,testStr))
print(re.search(myStr2,testStr)) #找到后返回object和他们的索引位置

#多种匹配
myStr3 = r"c[aA]t" #前面加一个r就是正则表达式匹配,括号里面代表可能是cat也可能是cAt
myStr4 = r"ca[t ts]" #前面加一个r就是正则表达式匹配
print(re.search(myStr3,testStr))
print(re.search(myStr4,testStr))

#复杂匹配
print(re.search(r"c[a-z]t",testStr))
print(re.search(r"c[A-Z]t",testStr))
print(re.search(r"c[0-9]t",testStr))
print(re.search(r"c[a-z 0-9]t",testStr))


print(re.search(r"t\dst","t9sting")) # \d代表数字, \D代表非数字
print(re.search(r"t\Dst","testing")) # \d代表数字, \D代表非数字

print(re.search(r"t\s\sst","t  sting")) # \s代表空白, \S代表非空白
print(re.search(r"t\Sst","t2sting")) # \s代表空白, \S代表非空白


print(re.search(r"^dog","dog eat cats")) # ^ 代表出现在句首才能匹配到
print(re.search(r"cats$","dog eat cats")) # $^ 代表出现在句尾才能匹配到


print(re.search(r"cat(s)?","dog eat cats")) # ()里面的s可能出现也可能不出现(可能cat也可能cats），但是都会匹配
print(re.search(r"(run|ran|ren|rkn)","dog eat cats and ren away")) # ()都可能出现，用|分开，比较常用