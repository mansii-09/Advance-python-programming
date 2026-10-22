class User:
    def __init__(self,username,email):
        self.username = username
        self.email = email

class Influencer(User):
    def __init__(self, username, email, followers):
        super().__init__(username, email)
        self.followers = followers

class VerifiedInfluencer(Influencer):
    def __init__(self, username, email, followers, badge):
        super().__init__(username, email, followers)
        self.badge = badge

v1 = VerifiedInfluencer(
    "mansi09", "mansi@gmail.com", 150000, "Blue Tick"
)

print(v1.username)
print(v1.email)
print(v1.followers)
print(v1.badge)