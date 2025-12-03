#Print 1 to 100 in snakes and ladder pattern.

num = 1
rows = 10
cols = 10

for r in range(1, rows + 1):

    row_numbers = [] 

    for c in range(cols):
        row_numbers.append(num)
        num += 1

    if r % 2 == 0:
        row_numbers.reverse()

    for x in row_numbers:
        print(f"{x:3}",end=" ")

    print()

