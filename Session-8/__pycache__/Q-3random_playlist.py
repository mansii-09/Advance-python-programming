import random 

songs = [
    "Kesariya",
    "Tum hi ho",
    "Heeriye",
    "chaleya",
    "perfect"
]

random.shuffle(songs)

print("random playlist:")

for song in songs:
    print(song)