#Accept no. of passengers from user and per ticket cost. Then accept age of each
#passenger and then calculate total amount to ticket to travel for all of them based on
#following condition :
#a. Children below 12 = 30% discount
#b. Senior citizen (above 59) = 50% discount
#c. Others need to pay full.

num_passengers = int(input("Enter no. of passengers:"))
ticket_cost = float(input("Enter cost of the ticket:"))

total_amount = 0

for i in range(1, num_passengers + 1):
    age = int(input(f"Enter age of passenger {i}:"))

    if age < 12:
        fare = ticket_cost * 0.7
    elif age > 59:
        fare = ticket_cost * 0.5
    else:
        fare = ticket_cost
    total_amount += fare
    print(f"Ticket amount for passenger {i}: RS.{fare:.2f}")
print(f"\nTotal amount to be paid for all passengers: Rs.{total_amount:.2f}")
