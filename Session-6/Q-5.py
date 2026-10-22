def format_followers(count):
    if count >= 1_000_000:
        return f"{count / 1_00_000:.1f}M"
    elif count >= 1_000:
        return f"{count / 1_000:.1f}K"
    else:
        return str(count)


class User:
    def __init__(self, username, email):
        self.username = username
        self.emial = email


class Influencer(User):
    def __init__(self, username, email, followers):
        super().__init__(username, email)
        self.followers = followers

class VerifiedInfluencer(Influencer):
    def __init__(self, username, email, followers, badge):
        super().__init__(username, email, followers)
        self.badge = badge

    def display_profile(self):
        print("Username:", self.username)
        print("Followers:", format_followers(self.followers))
        print("Verified:", self.badge)


v1 = VerifiedInfluencer(
    "mansi09", "mansi@gmail.com", 1500000, "Blue Tick"
)

v1.display_profile()