# Write a Python function that takes an email address as input and uses a regular
# expression to validate if it is a valid email address. The function should return True for
# valid emails and False for invalid ones.

import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

emails = [
    "test@example.com",
    "user.name@domain.co.in",
    "invalid@domain",
    "user@.com",
    "user@domain@com"
]

for e in emails:
    print(e, "->", is_valid_email(e))
