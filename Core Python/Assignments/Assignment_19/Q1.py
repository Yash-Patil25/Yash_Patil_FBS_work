#Assignment on Comprehension

#Find all of the numbers from 1–1000 that are divisible by 8

numbers = [num for num in range(1, 1001) if num % 8 == 0]
print(numbers) 