#Write a program find reverse of a number

def reverse_number(num):
    reverse = 0
    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit 
        num = num // 10
    return reverse

number = int(input("Enter Number:"))

print("Reverse number:",reverse_number(number))