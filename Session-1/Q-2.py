file = open("my_fav_songs.txt", "r")

songs = file.readlines()

for i, song in enumerate(songs, start=1):
    print(i, song.strip())

file.close()