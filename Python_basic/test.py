my_list = [1,2,3,4,5]

print(my_list)

my_list.append("ok")
print(my_list)

my_list.pop()
print(my_list)

#remove by value, not index
my_list.remove(3)
print(my_list)

my_list.append("raiden")
my_list.pop(len(my_list)-1)
print(my_list)

print(10 in my_list)


#while loop
price = 50

while price >=0:
    print(price)
    price = price - 1
    
    
d = {
    "a" : ["lion", 4],
    "b" : ["cat",3]
}
print(d["b"][1])

for i in range(5,8):
    print(i)
    



print(365%77)