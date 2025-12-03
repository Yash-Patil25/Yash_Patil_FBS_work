#Write a program to print all numbers which are divisible by m and n in the list.

size = int(input("Enter number of elements:"))
lst = []

i = 0
while i < size:
    num = int(input("Enter element: "))
    lst.append(num)
    i += 1

m = int(input("Enter value of m: "))
n = int(input("Enter value of n: "))

print("Numbers divisible by",m, "and",n,"are:")

i = 0
while i < size:
    if lst[i] % m == 0 and lst[i] % n == 0:
        print(lst[i])
    i += 1