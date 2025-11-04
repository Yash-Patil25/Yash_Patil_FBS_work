#g.
n = 5
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(2 * i - 1):
        print(chr(65 + j), end=" ")
    print()
