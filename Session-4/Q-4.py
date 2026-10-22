class InvalidSeatNumberError(Exception):
    pass

def book_ticket(movie, seat_number):
    if seat_number <= 0:
        raise InvalidSeatNumberError("Seat number must be positive")
    print("Ticket booked successfully")

book_ticket("Aveengers", -2)