#Write a program to create three lists of numbers, their squares and cubes.

n = int(input("Enter how many numbers you want: "))

numbers = []
squares = [] 
cubes = []

i = 0
while i < n:
    num = int(input("Enter Number:"))
    numbers.append(num)

    sq = num * num
    cu = num * num * num

    squares.append(sq)
    cubes.append(cu)

    i += 1

print("Numbers list:",numbers)
print("Squares list:",squares)
print("Cubes list:",cubes)

