try :
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))

    total = price * quantity

    print("Total amount:", total)

except ValueError:
    print("Error: Please enter a valid numeric value!")