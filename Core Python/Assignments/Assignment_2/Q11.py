#Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.
amount = int(input("Enter the amount: "))
notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

note_count = {}
for note in notes:
    if amount >= note:
        count = amount // note  
        amount = amount % note  
        note_count[note] = count
print("\nMinimum number of notes needed:")
for note, count in note_count.items():
    print(f"₹{note} : {count}")