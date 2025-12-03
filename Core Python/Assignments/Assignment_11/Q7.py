#Python Program to Find the Intersection of Two Lists

list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]

intersection_list = []

for x in list1:
    for y in list2:
        if x == y:
            if x not in intersection_list:
                intersection_list.append(x)

print("Intersection of two lists:", intersection_list)
