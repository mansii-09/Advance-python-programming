class Content:
    def display(self,title):
        print("Title:", title)

class Movie(Content):
    def display(self, title, year):
        print("Title:", title)
        print("Year:", year)

obj = Movie()
obj.display("3 Idiots", 2009)