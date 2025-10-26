#Write a program to input any alphabet and check whether it is vowel or consonant.
ch = input("Enter Alphabet:")

if ch.lower() in ['a','e','i','o','u']:
    print(f'{ch} is vowel.')
else:
    print(f'{ch} is a consonant.')