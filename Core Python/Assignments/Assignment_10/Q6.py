#Write a program to remove duplicates from the list.

nums = [10,10,20,30,40,40,50]

unique_list = []

for item in nums:
    if item not in unique_list:
        unique_list.append(item)
print("Original list:",nums)
print("List after removing duplicates:",unique_list)