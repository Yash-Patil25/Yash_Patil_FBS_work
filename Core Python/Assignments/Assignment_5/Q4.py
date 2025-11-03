#Write a program to check if given number is Armstrong number or not.
#(Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +
#4*4*4*4)

num = int(input("Enter Number:"))

num_str = str(num)
n = len(num_str)

sum_of_powers = 0
for digit in num_str:
    sum_of_powers += int(digit) ** n
if sum_of_powers == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")