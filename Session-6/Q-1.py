class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

u1 = User("mansi09", "mansi@gmail.com")

print("Username:", u1.username)
print("Email:", u1.email)