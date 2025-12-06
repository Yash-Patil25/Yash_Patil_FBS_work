#Python Program to Sum All the Items in a Dictionary

my_dict = {'a': 10,'b': 20,'c': 30,'d': 40}

total = 0

for value in my_dict.values():
    total += value

print("Sum of all items =",total)