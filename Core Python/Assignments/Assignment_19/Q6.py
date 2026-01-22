#Use a dictionary comprehension to count the length of each word in a sentence (take input from user)

sentence = input("Enter a sentence: ")

word_lengths = {word: len(word) for word in sentence.split()}
print(word_lengths)
