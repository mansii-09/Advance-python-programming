
# Base Class
class FestPass:
    def __init__(self, holder):
        self.holder = holder

    def price(self):
        return 500

    def perks(self):
        return "General entry access"

    def group_price(self, count=1, discount_percent=0):
        total = self.price() * count
        discount = total * discount_percent / 100
        return total - discount


# Student Pass
class StudentPass(FestPass):
    def price(self):
        return 300

    def perks(self):
        return "Student entry with basic facilities"


# Alumni Pass
class AlumniPass(FestPass):
    def price(self):
        return 800

    def perks(self):
        return "Alumni entry with networking access"


# VIP Pass
class VIPPass(FestPass):
    def price(self):
        return 2000

    def perks(self):
        return "VIP entry with premium seating and food"


# Testing One Object of Each Class
print("----- Pass Testing -----")

p1 = FestPass("Rahul")
p2 = StudentPass("Amit")
p3 = AlumniPass("Raj")
p4 = VIPPass("Ravi")

for p in [p1, p2, p3, p4]:
    print("Holder:", p.holder)
    print("Price: ₹", p.price())
    print("Perks:", p.perks())
    print("----------------------")


# Function to Print Receipt
def print_receipt(pass_obj):
    print("\n----- Pass Receipt -----")
    print("Holder Name:", pass_obj.holder)
    print("Price: ₹", pass_obj.price())
    print("Perks:", pass_obj.perks())


# List of 8 Passes
passes = [
    StudentPass("Amit"),
    StudentPass("Neha"),
    StudentPass("Riya"),
    AlumniPass("Raj"),
    AlumniPass("Karan"),
    VIPPass("Ravi"),
    FestPass("Meet"),
    FestPass("Jay")
]

print("\n----- All Pass Receipts -----")

total = 0

for p in passes:
    print_receipt(p)
    total += p.price()

print("\nTotal Pass Amount: ₹", total)


# Group Price Testing
print("\n----- Group Price Testing -----")

student = StudentPass("Mansi")
alumni = AlumniPass("Rahul")

print("Student group_price():", student.group_price())
print("Student group_price(4):", student.group_price(4))
print("Student group_price(4, 10):", student.group_price(4, 10))

print("Alumni group_price(2, 25):", alumni.group_price(2, 25))


# Registration Menu
print("\n----- Fest Pass Registration -----")

pass_types = {
    "G": FestPass,
    "S": StudentPass,
    "A": AlumniPass,
    "V": VIPPass
}

registrations = []

while True:
    holder = input("Enter holder name: ")

    print("G - General Pass")
    print("S - Student Pass")
    print("A - Alumni Pass")
    print("V - VIP Pass")

    choice = input("Enter pass type: ").upper()

    if choice not in pass_types:
        print("Invalid pass type!")
        continue

    count = int(input("Enter count: "))
    discount = float(input("Enter discount percentage: "))

    pass_class = pass_types[choice]
    obj = pass_class(holder)

    amount = obj.group_price(count, discount)

    registrations.append({
        "type": choice,
        "holder": holder,
        "count": count,
        "amount": amount
    })

    more = input("Add another registration? (yes/no): ").lower()

    if more != "yes":
        break


# Per-Type Total and Grand Total
print("\n----- Final Registration Report -----")

type_totals = {
    "G": 0,
    "S": 0,
    "A": 0,
    "V": 0
}

grand_total = 0

for r in registrations:
    type_totals[r["type"]] += r["amount"]
    grand_total += r["amount"]

print("General Total: ₹", type_totals["G"])
print("Student Total: ₹", type_totals["S"])
print("Alumni Total: ₹", type_totals["A"])
print("VIP Total: ₹", type_totals["V"])

print("--------------------------")
print("Grand Total: ₹", grand_total)
