#Python Program to Sort a List According to the Length of the Elements within the list.

words = ["apple","cat","banana","dog","elephant"]

for i in range(len(words)):
    for j in range(len(words) - i - 1):
        if len(words[j]) > len(words[j + 1]):

            temp = words[j]
            words[j] = words[j + 1]
            words[j + 1] = temp
            
print("sorted list by length:",words)