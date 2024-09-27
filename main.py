units = int(input("Please Enter the number of units used:"))

if units<30:
    amount = 1.10 * units
    tax = 10
elif units<=100:
    amount = 5.56
else:
    amount = 6.23
    tax = 89

total = amount+tax
print("Electricity bill is:",total)