#Python Program to count number of digits and letters in a string.

string = input("Enter String:")

digit_count = 0
letter_count = 0

for ch in string:
    if '0' <= ch <= '9':
        digit_count += 1
    elif ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
        letter_count += 1

print("No. of letter:",letter_count)
print("No. of digits:",digit_count)