#Python Program to Find the Union of two Lists

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

union_list = []

for x in list1:
    if x not in union_list:
        union_list.append(x)

for y in list2:
    if y not in union_list:
        union_list.append(y)

print("Union of two lists:",union_list)