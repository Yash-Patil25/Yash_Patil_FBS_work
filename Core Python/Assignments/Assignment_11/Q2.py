#2. Python Program to Merge Two Lists and Sort it

list1 = [5,1,9,3]
list2 = [8,2,7,6]

merged_list = []

for x in list1:
    merged_list.append(x)

for y in list2:
    merged_list.append(y)

for i in range(len(merged_list)):
    for j in range(len(merged_list) - i - 1):
        if merged_list[j] > merged_list[j + 1]:
            temp = merged_list[j]
            merged_list[j] = merged_list[j + 1]
            merged_list[j + 1] = temp

print("Merged and Sorted List: ",merged_list)