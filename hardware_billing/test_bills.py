
from hardware_shop.bill_numbers import new_bill_number

bills = []

for i in range(20):
    bill = new_bill_number()
    bills.append(bill)
    print(bill)

# Check Duplicates
if len(bills) == len(set(bills)):
    print("Duplicates: 0")
else:
    print("Duplicates found!")
