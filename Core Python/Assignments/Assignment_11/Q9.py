#Write a program to create three lists of numbers, their squares and cubes.

numbers = [1, 2, 3, 4, 5]

squares = []
cubes = []

for n in numbers:
    squares.append(n * n)      
    cubes.append(n * n * n)    

print("Numbers :", numbers)
print("Squares :", squares)
print("Cubes   :", cubes)
