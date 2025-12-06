#Python Program to Concatenate Two Dictionaries Into One

dict1 = {1: "apple", 2: "banana"}
dict2 = {3: "cherry", 4: "mango"}

result = {}

for key in dict1:
    result[key] = dict1[key]

for key in dict2:
    result[key] = dict2[key]

print("Concatenated Dictionary:",result)