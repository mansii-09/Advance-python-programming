def get_song_duration(song_name):
    songs = {
        "Shape of You" : "3.53",
        "Perfect" : "4.23",
        "Believer" : "3.24"
    }

    try:
        print(songs[song_name])

    except KeyError:
        print("Song not found on spotify!")

get_song_duration("Perfect")
get_song_duration("Hello")