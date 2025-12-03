#Write a program to find maximum and minimum element in a list.

nums = [12,5,89,34,2,77]

maximum = nums[0]
minimum = nums[0]

for x in nums:
    if x > maximum:
        maximum = x
    if x < minimum:
        minimum = x
print("Maximum element =",maximum)
print("Mininum element =",minimum)

