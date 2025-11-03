#Write a program to accept an integer amount from user and tell minimum
#number of notes needed for representing that amount. (Use looping to optimize
#the problem)

amount = int(input("Enter the amount: "))

notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

print("\nMinimum number of notes required:")

total_notes = 0

for note in notes:
    count = amount // note 
    if count > 0:
        print(f"{note} x {count}")
        total_notes += count
        amount = amount % note 

print(f"\nTotal notes needed: {total_notes}")
