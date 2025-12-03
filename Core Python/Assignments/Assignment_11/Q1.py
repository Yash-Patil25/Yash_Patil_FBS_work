#Python Program to Put Even and Odd elements of a List into two Different Lists.

nums = [12,7,5,64,14,9,21,32]

even_list = []
odd_list = []

for n in nums:
    if n % 2 == 0:
        even_list.append(n)
    else:
        odd_list.append(n)

print("Even numbers:",even_list)
print("odd numbers:",odd_list)