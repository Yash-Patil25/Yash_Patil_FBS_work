# #Regular Expression.

# Develop a function that takes a text and a list of forbidden words. Replace all
# occurrences of these forbidden words with asterisks (*) using regular expressions.

import re

def censor_text(text, forbidden_words):

    pattern = r'\b(' + '|'.join(map(re.escape, forbidden_words)) + r')\b'

    censored_text = re.sub(
        pattern,
        lambda match: '*' * len(match.group()),
        text,
        flags=re.IGNORECASE
    )

    return censored_text

text = "Python is easy and Java is powerful. I like Java."
forbidden_words = ["java", "easy"]

result = censor_text(text, forbidden_words)
print(result)
