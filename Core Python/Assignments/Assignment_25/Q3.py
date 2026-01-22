# #Develop a function that counts the occurrences of each word in a given text. Use regular
# expressions to split the text into words and then count the frequency of each word.

import re
from collections import defaultdict

def word_frequency(text):
    # Extract words using regex (ignores punctuation)
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())

    frequency = defaultdict(int)
    for word in words:
        frequency[word] += 1

    return dict(frequency)

text = "Python is easy. Python is powerful, and Python is popular!"
result = word_frequency(text)

for word, count in result.items():
    print(f"{word}: {count}")
