file = open("my_fav_songs.txt","r")

songs = file.readlines()

print("total songs:", len(songs))

file.close()