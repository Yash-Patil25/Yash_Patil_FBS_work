#Write a program to calculate profit or loss.
cost_price = float(input("Enter Cost Price:"))
selling_price = float(input("Enter Selling Price:"))

if selling_price > cost_price:
    profit = selling_price - cost_price
    print("Profit:",profit)
elif cost_price > selling_price:
    loss = cost_price - selling_price
    print("Loss:",loss)
else:
    print("No Profit No Loss!!!")