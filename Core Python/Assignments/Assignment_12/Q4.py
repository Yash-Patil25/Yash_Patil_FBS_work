#Python Program to Form a New String where the First Character and the Last Character have been Exchanged

s = input("Enter String:")

if len(s) <= 1:
    print("New String:",s)
else:
    new_str = s[-1] + s[1:-1] + s[0]
    print("New string:",new_str)