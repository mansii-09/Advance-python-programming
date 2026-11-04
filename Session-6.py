
# Base Class
class Vehicle:
    def __init__(self, reg_no, owner, hours, rate):
        self.reg_no = reg_no
        self.owner = owner
        self.hours = hours
        self.rate = rate

    def parking_charge(self):
        return self.hours * self.rate


# Child Class - Two Wheeler
class TwoWheeler(Vehicle):
    def __init__(self, reg_no, owner, hours):
        super().__init__(reg_no, owner, hours, 10)


# Child Class - Four Wheeler
class FourWheeler(Vehicle):
    def __init__(self, reg_no, owner, hours):
        super().__init__(reg_no, owner, hours, 30)


# Electric Car inherits FourWheeler
class ElectricCar(FourWheeler):
    def __init__(self, reg_no, owner, hours, battery_kwh):
        super().__init__(reg_no, owner, hours)
        self.battery_kwh = battery_kwh

    def charging_cost(self, units):
        return units * 12


# Valet Service Class
class ValetService:
    def valet_fee(self):
        return 50


# Multiple Inheritance
class ValetElectricCar(ElectricCar, ValetService):
    def __init__(self, reg_no, owner, hours, battery_kwh):
        ElectricCar.__init__(self, reg_no, owner, hours, battery_kwh)

    def bill(self, units):
        return (
            self.parking_charge()
            + self.charging_cost(units)
            + self.valet_fee()
        )


# Testing Part

print("----- Parking Charge Testing -----")

car = FourWheeler("GJ01AB1234", "Rahul", 3)
print("Four Wheeler Parking:", car.parking_charge())

bike = TwoWheeler("GJ01CD5678", "Amit", 5)
print("Two Wheeler Parking:", bike.parking_charge())

electric = ElectricCar("GJ01EF1234", "Raj", 2, 60)
print("Electric Car Parking:", electric.parking_charge())
print("Charging Cost:", electric.charging_cost(10))

valet_car = ValetElectricCar("GJ01GH1234", "Ravi", 2, 75)
print("Valet Electric Car Bill:", valet_car.bill(10))


# Day-End Report

vehicles = [
    Vehicle("GJ01AA1111", "A", 2, 20),
    TwoWheeler("GJ01BB2222", "B", 5),
    FourWheeler("GJ01CC3333", "C", 3),
    ElectricCar("GJ01DD4444", "D", 2, 60),
    ValetElectricCar("GJ01EE5555", "E", 2, 75),
    TwoWheeler("GJ01FF6666", "F", 4),
    FourWheeler("GJ01GG7777", "G", 5),
    ElectricCar("GJ01HH8888", "H", 3, 80)
]

print("\n----- Day End Parking Report -----")

total_revenue = 0

for vehicle in vehicles:
    charge = vehicle.parking_charge()

    print("Class:", type(vehicle).__name__)
    print("Registration No:", vehicle.reg_no)
    print("Parking Charge: ₹", charge)
    print("-------------------------")

    total_revenue += charge

print("Total Parking Revenue: ₹", total_revenue)
