class Payment:
    def pay(self,amount):
        print("Paying", amount)

class UPI(Payment):
    def pay(self,amount):
        print("Playing", amount, "Via UPI")

obj1 = Payment()
obj2 = UPI()

obj1.pay(1000)
obj2.pay(500)