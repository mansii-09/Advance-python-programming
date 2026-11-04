
import hardware_shop.stock as stock

# Check Stock
print("Available Stock:")
print(stock.check_stock("Cement"))

# Reduce Stock
try:
    price = stock.reduce_stock("Cement", 5)
    print("Stock Reduced Successfully!")
    print("Price Per Box:", price)

except stock.OutOfStockError as e:
    print("Error:", e)


# Failing Request
try:
    stock.reduce_stock("Paint", 100)

except stock.OutOfStockError as e:
    print("Error:", e)
