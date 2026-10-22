class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

class Influencer(User):
    def __init__(self, username, email, followers):
        super().__init__(username, email)
        self.followers = followers

il = Influencer("masni09", "mansi@gmail.com", 5000)

print(il.username)
print(il.email)
print(il.followers)