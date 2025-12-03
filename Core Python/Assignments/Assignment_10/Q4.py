#Write a program to reverse the list.

nums = [10,20,30,40,50]
rev_list = []

for i in range(len(nums) -1,-1,-1):
    rev_list.append(nums[i])

print('Original list :', nums)
print('Reverse List :',rev_list)