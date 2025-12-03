#Write a program to remove all occurrences of a given element in the list.

n = int(input("Enter number of elements:"))

lst = [0] * n
print("Enter elements:")
for i in range(n):
    lst[i] = int(input())

x = int(input("Enter element to remove:"))

new_list = [0] * n
index = 0

for i in range(n):
    if lst[i] != x:
        new_list[index] = lst[i]
        index += 1

print("Original list:",lst)

print("List after removing all occurrences of",x,":",end=" ")
for i in range(index):
    print(new_list[i],end = " ")
