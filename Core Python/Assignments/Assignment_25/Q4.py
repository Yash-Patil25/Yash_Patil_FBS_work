# #Write a function that extracts all the URLs from a given text using regular expressions.
# Return a list of URLs found in the input text.

import re

def extract_urls(text):
    url_pattern = r'https?://[^\s,]+'
    return re.findall(url_pattern, text)

text = """
Visit https://www.google.com for search,
check http://example.org/page,
or go to https://openai.com.
"""

urls = extract_urls(text)
print(urls)
