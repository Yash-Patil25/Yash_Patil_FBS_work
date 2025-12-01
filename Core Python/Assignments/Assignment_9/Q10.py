# Write a program to reverse a number using recursion.
def reverse_num(n, rev=0):
    if n == 0:
        return rev
    digit = n % 10
    rev = rev * 10 + digit
    return reverse_num(n // 10, rev)

num = int(input("Enter a number: "))
print("Reversed number is:", reverse_num(num))
