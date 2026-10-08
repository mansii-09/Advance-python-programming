file = open("orders.txt", "r")

while True:
    order = file.readline()

    if order == "":
        break

    print("Order:", order.strip())
    print("File pointer position:", file.tell())

file.close()
