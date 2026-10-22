class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

s1 = Song("Kesariya", "Arjit Singh", 250)
s2 = Song("Apna Bana Le", "Arjit Singh", 230)

print(s1.title, s1.artist, s1.duration)
print(s2.title, s2.artist, s2.duration)