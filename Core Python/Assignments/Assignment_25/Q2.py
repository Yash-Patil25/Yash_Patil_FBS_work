# #Create a function that extracts all the dates from a given text using regular expressions.
# Dates can be in various formats like MM/DD/YYYY, DD-MM-YYYY, or written out like

import re

def extract_dates(text):
    dates_pattern = [
        r'\b/d{2}/\d{2}/\d{4}\b',
        r'\b/d{2}-\d{2}-/d{4}\b',
        r'\b(?:January|February|March|April|May|June|'
        r'July|August|September|October|November|December)\s'
        r'\d{1,2},\s\d{4}\b'
    ]
    dates = []
    for pattern in date_patterns:
        dates.extend(re.findall(pattern, text))

    return dates

text = """
The event is on 01/15/2024.
The deadline was 15-01-2024.
Another meeting happened on January 1, 2023.
"""

print(extract_dates(text))
