#Write a Python program to find all the unique combinations of 3 numbers from a given list of numbers, adding up to a target number.

numbers = [1, 2, -1, 0, -2, 3]
target = 3

result = set()

n = len(numbers)

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if numbers[i] + numbers[j] + numbers[k] == target:
                
                combo = tuple(sorted((numbers[i], numbers[j], numbers[k])))
                result.add(combo)


print("Unique combinations of 3 numbers with sum", target, ":")
for comb in result:
    print(comb)
