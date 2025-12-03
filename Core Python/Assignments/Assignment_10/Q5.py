#Accept a number from user and check if this element is present in the list or
#not. Also tell how many times it is present in the list.

nums = [10,20,30,20,40,20,40,50,10]

n = int(input("Enter number to search:"))

count = 0

for x in nums:
    if x == n:
        count += 1

if count > 0:
    print(n, "is present in the list")
    print("It appears",count,"times.")
else:
    print(n,"is NOT present in list.")