class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

class Influencer(User):
    def __init__(self, username, email, followers):
        super().__init__(username, email)
        self.followers = followers

class Brand:
    def __init__(self,brand_name):
        self.brand_name = brand_name

class BrandPartner(Influencer, Brand):
    def __init__(self, username, email, followers, brand_name):
        Influencer.__init__(self, username, email, followers)
        Brand.__init__(self, brand_name)

b1 = BrandPartner("mansi09", "mansi@gmail.com", 50000, "Nike")

print(b1.username)
print(b1.followers)
print(b1.brand_name)
