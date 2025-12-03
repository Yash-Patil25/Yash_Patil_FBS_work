#Write a program of having n number of elements in the list and find out even
#and odd elements in that list and then create two separate lists which will have
#even elements and other will have odd elements.

n = int(input("Enter how many elements:"))

numbers = []
for i in range(n):
    num = int(input(f"Enter element {i+1}:"))
    numbers.append(num)

even_list = []
odd_list = []

for item in numbers:
    if item % 2 == 0:
        even_list.append(list)
    else:
        odd_list.append(list)

print("Original List:",numbers)
print("Even Element list:",even_list)
print("Odd Element list:",odd_list)