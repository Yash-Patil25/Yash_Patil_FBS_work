#Sum of all prime numbers between 1 to n

def is_prime(num):
    if num >= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def sum_of_primes(num):
    total = 0
    for num in range(2, num+1):
        if is_prime(num):
            total += num
    return total

n = int(input("Enter a number:"))
print("sum of all prime numbers between 1 and",n,"is:",sum_of_primes(n))