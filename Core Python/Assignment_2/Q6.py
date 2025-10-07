#WAP to calculate total salary of employee based on basic, da=10% of basic,ta=12% of basic, hra=15% of basic.
basic = float(input("Enter basic salary of emp:"))

da = 0.10 * basic  #Dearness allowance 10%
ta = 0.12 * basic  #Travel allowance 12%
hra = 0.15 * basic  #House rent allownace 15%

total_salary = basic + da + ta + hra

print("\n --- Salary Details ---")
print("Basic salary =",basic)
print("DA (10%) =",da)
print("TA (12%) ",ta)
print("HRA (15%) =",hra)
print("Total Salary =",total_salary)        