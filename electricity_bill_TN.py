# Electricity Billing System - Tamil Nadu

def calculate_bill(units):

    if units <= 100:
        bill = 0

    elif units <= 200:
        bill = 0

    elif units <= 300:
        bill = (units - 200) * 4.70

    elif units <= 500:
        bill = (100 * 4.70) + (units - 300) * 6.30

    else:
        bill = (200 * 4.70) + (100 * 6.30) + (units - 300) * 8.40

    return bill


n = int(input("Enter number of customers: "))

for i in range(1, n + 1):
    print(f"\nCustomer {i}")

    name = input("Enter customer name: ")
    units = float(input("Enter units consumed: "))

    bill = calculate_bill(units)

    print("Customer Name :", name)
    print("Units         :", units)
    print("Bill Amount   : Rs.", round(bill, 2))