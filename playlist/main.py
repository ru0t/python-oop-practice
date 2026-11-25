import random


class Song:
    def __init__(self, title):
        self.title = title


class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def delete_song(self, song):
        if song in self.songs:
            self.songs.remove(song)

    def shuffle_songs(self):
        random.shuffle(self.songs)

    def __str__(self):
        return f"Playlist: {", ".join(self.songs)}"


playlist = Playlist()
playlist.add_song("Blinding Lights")
playlist.add_song("Levitating")
playlist.add_song("Peaches")
playlist.add_song("What You Heard")
playlist.add_song("Next To You")

playlist.shuffle_songs()
print(playlist)

playlist.delete_song("Peaches")
print(playlist)
