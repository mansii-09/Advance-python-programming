
# Import Statements
import hardware_shop.pricing as pricing

from hardware_shop.stock import reduce_stock, OutOfStockError

from hardware_shop import new_bill_number


# Customer Billing Function
def generate_bill(customer, item, boxes):

    print("\n----------------------------")
    print("Customer Name:", customer)

    try:
        # Reduce Stock and Get Price
        price = reduce_stock(item, boxes)

        # Calculate Amount
        amount = price * boxes

        # Calculate GST
        gst = pricing.gst_amount(amount)

        # Calculate Final Total
        total = amount + gst

        # Round Down to Multiple of 5
        final_total = pricing.round_down_to_five(total)

        # Generate Bill
        bill_no = new_bill_number()

        print("Bill Number:", bill_no)
        print("Item:", item)
        print("Boxes:", boxes)
        print("Price Per Box: ₹", price)
        print("Amount: ₹", amount)
        print("GST: ₹", gst)
        print("Final Total: ₹", final_total)

    except OutOfStockError as e:
        print("Bill Cannot Be Generated!")
        print("Reason:", e)

    print("----------------------------")


# Three Customer Bills

generate_bill("Mansi", "Cement", 5)

generate_bill("Rahul", "Paint", 2)

generate_bill("Priya", "Bricks", 150)
