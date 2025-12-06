#Python Program to Detect if Two Strings are Anagrams

s1 = input("First String:")
s2 = input("Second String:")

s1 = s1.replace(" ", " ").lower()
s2 = s2.replace(" ", " ").lower()

if sorted(s1) == sorted(s2):
    print("strings are Anagrams")
else:
    print("Not Anagrams")