class ZomatoOrder:
    def add_item(self, item, quantity=1):
        print("Item:", item)
        print("Quantity:", quantity)

obj = ZomatoOrder()

obj.add_item("Pizza")
obj.add_item("Burger",3)