#Write a program to create a new list from existing list which contains cube of each number of list.

nums = [1,2,3,4,5]

cubes = []

for num in nums:
    cubes.append(num ** 3)
print("Original List:",nums)
print("List of cubes:",cubes)