#String
#Python Program to Replace all Occurrences of ‘a’ with $ in a String

s = input('Enter String:')

new_str = ""
for char in s:
    if char == 'a':
        new_str += '$'
    else:
        new_str += char

print("Modified String:",new_str)