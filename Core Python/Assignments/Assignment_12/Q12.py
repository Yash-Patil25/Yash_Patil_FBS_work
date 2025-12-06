#Python Program to count number of lowercase characters in a string.

string = input("Enter String:")

count = 0
for ch in string:
    if 'a' <= ch <= 'z':
        count += 1

print("Number of lowercase characters:",count)