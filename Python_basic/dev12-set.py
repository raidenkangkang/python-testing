'''
set testing, contain all info, 
changeable set: no-order, can not have duplicated values
frozenset: can't change the value at all, like the tuple
'''

#...
my_set = set("hello")
my_set2 = set("raiden")

#only show number e as they both in
print(my_set&my_set2)