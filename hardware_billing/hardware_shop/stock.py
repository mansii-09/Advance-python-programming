
# Custom Exception
class OutOfStockError(Exception):
    pass


# Hardware Stock Dictionary
hardware_items = {
    "Cement": {"quantity": 20, "price": 350},
    "Paint": {"quantity": 15, "price": 500},
    "Bricks": {"quantity": 100, "price": 8},
    "Tiles": {"quantity": 30, "price": 600},
    "Pipes": {"quantity": 25, "price": 250},
    "Nails": {"quantity": 40, "price": 100},
    "Wires": {"quantity": 18, "price": 450},
    "Bolts": {"quantity": 50, "price": 120}
}


# Check Stock
def check_stock(item):
    if item not in hardware_items:
        raise OutOfStockError("Item not found!")

    return hardware_items[item]


# Reduce Stock
def reduce_stock(item, qty):
    if item not in hardware_items:
        raise OutOfStockError("Item not found!")

    if qty > hardware_items[item]["quantity"]:
        raise OutOfStockError("Not enough stock available!")

    if qty <= 0:
        raise OutOfStockError("Quantity must be greater than zero!")

    hardware_items[item]["quantity"] -= qty

    return hardware_items[item]["price"]
