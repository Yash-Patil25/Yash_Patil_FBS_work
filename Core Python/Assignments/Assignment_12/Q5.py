#Python Program to Count the Number of Vowels in a String.

str = input("Enter String:")

vowels = 'aeiouAEIOU'
count = 0

for ch in str:
    if ch in vowels:
        count += 1

print("Number of vowels in the string:",count)
        