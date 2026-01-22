#Count the number of spaces in a string (take input from user)

text = input("enter  string:")

space_count = 0
for ch in text:
    if ch == ' ':
        space_count += 1

print("Number of spaces:", space_count)