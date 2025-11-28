#WAP to check if a given number is Armstrong number or not. For
#each task create separate functions.

def is_armstrong(num):
    digits = str(num)
    power = len(digits)
    total = 0
    
    for d in digits:
        total += int(d) ** power
    
    if total == num:
        return True
    else:
        return False

number = int(input("Enter a number: "))

if is_armstrong(number):
    print(number, "is an Armstrong number")
else:
    print(number, "is not an Armstrong number")
