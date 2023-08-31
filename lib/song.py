class Song:

    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre) -> None:
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if cls.genre_count.get(genre):
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if cls.artist_count.get(artist):
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1



# Creating instances of Song
ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
another_song = Song("Another Song", "Taylor Swift", "Pop")
yet_another_song = Song("Yet Another Song", "Jay-Z", "Rap")

# Checking counts
print(Song.count)  # Output: 3
print(Song.genres)  # Output: ['Rap', 'Pop']
print(Song.artists)  # Output: ['Jay-Z', 'Taylor Swift']

# Checking genre count
print(Song.genre_count)  # Output: {'Rap': 2, 'Pop': 1}

# Checking artist count
print(Song.artist_count)  # Output: {'Jay-Z': 2, 'Taylor Swift': 1}
