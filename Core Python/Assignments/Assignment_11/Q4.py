#Python Program to Find the Second Largest Number in a List Using Bubble Sort

nums = [12, 5, 9, 21, 7, 15]

for i in range(len(nums)):
    for j in range(len(nums) - i - 1):
        if nums[j] > nums[j + 1]:

            temp = nums[j]
            nums[j] = nums[j + 1]
            nums[j + 1] = temp

second_largest = nums[-2]

print("Second largest number:",second_largest)