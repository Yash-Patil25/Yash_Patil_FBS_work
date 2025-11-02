# WAP to print Armstrong number within a given range

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print("Armstrong numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
    digits = len(str(num))
    sum = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        sum += digit ** digits
        temp //= 10

    if num == sum:
        print(num)
