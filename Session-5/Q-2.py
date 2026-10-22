class FoodOrder:
    def __init__(self, restaurant_name, items, total_price):
        self.restaurant_name = restaurant_name
        self.items = items
        self.total_price = total_price

    def show_order(self):
        print("Restaurant:", self.restaurant_name)
        print("Items:", self.items)
        print("TOtal Price:", self.total_price)

order = FoodOrder("Domino's", ["Burger", "Pizza"], 350)
order.show_order()