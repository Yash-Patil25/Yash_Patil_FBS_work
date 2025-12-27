#Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value.

numbers = [2, 4, 3, 5, 7, 8, 9]
target_sum = 10

pairs = []

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target_sum:
            pairs.append((numbers[i], numbers[j]))

print("Pairs with sum", target_sum, "are:")
for pair in pairs:
    print(pair)
