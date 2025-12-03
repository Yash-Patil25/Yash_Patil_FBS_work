#Write a program to print list after removing even numbers.

nums = [12,7,5,64,14,9,21,32]

odd_list = []

for n in nums:
    if n % 2 != 0:
        odd_list.append(n)

print("List after removing even numbers:",odd_list)