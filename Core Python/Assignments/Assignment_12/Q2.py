#Python Program to Remove the nth Index Character from a Non-Empty String

s = input('Enter Non-Empty string:')
n = int(input("Enter the index to remove:"))

new_str = ""
for i in range(len(s)):
    if i != n:
        new_str += s[i]

print("string after removing char at index",n,":",new_str)