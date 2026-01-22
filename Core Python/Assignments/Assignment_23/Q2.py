# Build a currency converter application that converts between different currencies. The
# user should be able to enter an amount, select the input currency, select the output
# currency, and see the converted amount.


rates = {
    "INR": 1,
    "USD": 83,
    "EUR": 90,
    "GBP": 105
}

print("Available Currencies:")
print("INR, USD, EUR, GBP")

try:
    amount = float(input("Enter amount: "))
    from_currency = input("From currency: ").upper()
    to_currency = input("To currency: ").upper()

    if from_currency not in rates or to_currency not in rates:
        raise ValueError("Invalid currency selection")

    amount_in_inr = amount * rates[from_currency]
    converted_amount = amount_in_inr / rates[to_currency]

    print(f"Converted Amount: {converted_amount:.2f} {to_currency}")

except ValueError as e:
    print("Error:", e)
