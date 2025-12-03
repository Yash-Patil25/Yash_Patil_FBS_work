#Write a program to create a duplicate of an existing list. It should not point to same list.

original_list = [10,20,30,40,50]
duplicate_list = []

for item in original_list:
    duplicate_list.append(item)

print("Original list:",original_list)
print("Duplicate list:",duplicate_list)

print("Are both lists same?",original_list is duplicate_list)