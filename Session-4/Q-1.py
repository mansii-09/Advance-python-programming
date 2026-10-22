class InvalidCouponCodeError(Exception):
    pass

valid_coupons = ["ZOMATO50", "FOOD20"]

def apply_coupon(code):
    if code not in valid_coupons:
        raise InvalidCouponCodeError("Invalid coupon code")
    print("Coupon applied successfully")

apply_coupon("ABC123")