#Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary

text = input("Enter string:")

words = text.split()
freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print("word frequency:",freq)