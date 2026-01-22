#Find all of the words in a string that are less than 5 letters (take input from user)

text = input("Enter a string: ")

words = text.split()
result = []

for word in words:
    if len(word) < 5:
        result.append(word)

print("Words with less than 5 letters:", result)
