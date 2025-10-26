#11. Accept age of five people and also per person ticket amount and then calculate total
#amount to ticket to travel for all of them based on following condition :
#a. Children below 12 = 30% discount
#b. Senior citizen (above 59) = 50% discount
#c. Others need to pay full.

total_amount = 0
for i in range(1,6):
    print(f"\nperson {i}")
    age = int(input("Enter age:"))
    ticket_amount = float(input("Enter ticket amount:"))

    if age < 12:
        discount = 0.30 * ticket_amount
    elif age > 59:
        dicount = 0.50 * ticket_amount
    else:
        discount = 0
    final_amount = ticket_amount - discount
    total_amount += final_amount
    print(f"Amount to pay for person {i}:{final_amount}")
print(f"\nTotal amount to pay for all 5 people:{total_amount}")
    