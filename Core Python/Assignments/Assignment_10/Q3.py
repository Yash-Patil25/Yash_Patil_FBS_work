#Write a program to find the second largest element in the list.

nums = [12, 45, 77, 89, 34, 23]

largest = second_largest = -999999999
for x in nums:
    if x > largest:
        second_largest = largest
        largest = x
    elif x > second_largest and x != largest:
        second_largest = x
print("second largest element =",second_largest)
