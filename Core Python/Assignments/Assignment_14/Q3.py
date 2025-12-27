#Write a Python program to find all the unique words and count the frequency of occurrence from a given list of strings. Use Python set data type.

strings = [
    "python is easy",
    "python is powerful",
    "easy to learn python"
]

words = []

for sentence in strings:
    words.extend(sentence.split())

unique_words = set(words)

word_frequency = {}

for word in unique_words:
    word_frequency[word] = words.count(word)

print("Unique words and their frequencies:")
for word, count in word_frequency.items():
    print(word, ":", count)
