#Write a Python program to find the two numbers whose product is maximum among all the pairs in a given list of numbers. Use the Python set.

numbers = [1, 10, -5, 1, -100]

num_set = set(numbers)

num_list = list(num_set)

max_product = None
pair = ()

for i in range(len(num_list)):
    for j in range(i + 1, len(num_list)):
        product = num_list[i] * num_list[j]

        if max_product is None or product > max_product:
            max_product = product
            pair = (num_list[i], num_list[j])

print("Pair with maximum product:", pair)
print("Maximum product:", max_product)


