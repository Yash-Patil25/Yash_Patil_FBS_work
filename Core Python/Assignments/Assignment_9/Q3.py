#Write a program to reverse a given number using recursive function.

def reverse_num(n, rev=0):
    if n == 0:
        return rev
    return reverse_num(n // 10, rev * 10 + (n % 10))
1
num = int(input("Enter a number: "))
result = reverse_num(num)
print("Reversed number is:", result)
