#Write a program to print first n prime numbers.

num = int(input("Enter how many prime numbers you want: "))

count = 0       

print(f"First {num} prime numbers are:")

while count < num:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):   
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")
        count += 1

    num += 1
