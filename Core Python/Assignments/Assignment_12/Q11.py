#Python Program to replace every blank space with hyphen in a string.

string = input("Enter String:")

new_string = ""
for ch in string:
    if ch == " ":
        new_string += "-"
    else:
        new_string += ch

print("String after replacing spaces with hypens:",new_string)

