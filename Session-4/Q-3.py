class PaymentFailedError(Exception):
    pass

def process_payment(amount):
    if amount <= 0:
        raise PaymentFailedError("Invalid payment amount")
    print("Payment Successful")

process_payment(500)