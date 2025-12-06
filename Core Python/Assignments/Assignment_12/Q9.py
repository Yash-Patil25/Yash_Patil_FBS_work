#Python Program to Calculate the Number of Words and the Number of Characters Present in a String

string = input("Enter String:")

char_count = 0
for ch in string:
    char_count += 1

word_count = 0
in_word = False

for ch in string:
    if ch != " " and not in_word:
        word_count += 1
        in_word = True
    elif ch == " ":
        in_word = False

print("NUmber of characters (including spaces):",char_count)
print("Number of words:",word_count)