def book_movie_ticket(tickets):
    wallet_balance = 1000

    try:
        price_per_ticket = wallet_balance / int(tickets)
        print("Price per ticket:", price_per_ticket)

    except ZeroDivisionError:
        print("Error: Number of tickets cannot be Zero!")

    except ValueError:
        print("Error: Please enter a valid number!")

book_movie_ticket(5)
book_movie_ticket(0)
book_movie_ticket("abc")