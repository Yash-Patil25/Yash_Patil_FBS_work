#Write a program to check if entered number is a palindrome or not.

def is_pallindrome(num):
    original_num = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    return original_num == reverse

number = int(input("Enter Number:"))

if is_pallindrome(number):
    print(number,"is a pallindrome")
else:
    print(number,"is not a pallindrome")