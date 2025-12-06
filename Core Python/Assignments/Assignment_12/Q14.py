#Python Program to count the occurrences of ach word in a string.

string = input("Enter String:")

words = [] 
word = ""

for ch in string:
    if ch != " ":
        word += ch
    else:
        if word != "":
            words.append(word)
            word = ""

if word != "":
    words.append(word)

word_count = {}

for w in words:
    if w in word_count:
        word_count[w] += 1
    else:
        word_count[w] = 1

print("Occurrences of each word:")
for w in word_count:
    print(w, ":",word_count[w])

