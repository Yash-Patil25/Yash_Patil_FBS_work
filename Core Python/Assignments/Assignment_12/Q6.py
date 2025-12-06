#Python Program to Take in a String and Replace Every Blank Space with Hyphen

string = input("Enter String:")

new_string = ""

for ch in string:
    if ch == " ":
        new_string += "-"
    else:
        new_string += ch

print("String after replacing spaces with hyphens:")
print(new_string)