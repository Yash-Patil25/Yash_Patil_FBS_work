#Remove all of the vowels in a string (take input from user)

text = input("Enter a string: ")

result = ""
for ch in text:
    if ch.lower() not in "aeiou":
        result += ch

print("String without vowels:", result)
