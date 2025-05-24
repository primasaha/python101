def make_album(artist_name, album_title, number_of_songs):
    album = {
        "artist": artist_name,
        "title": album_title
    }
while True:
    print("\nEnter album information (type 'q' at any time to quit): ")
    artist = input("Artist name: ")
    if artist.lower() == 'q':
        break

    title = input("Album title: ")
    if title.lower() == 'q':
        break

    songs = input("Number of songs : ")
    if songs.lower() == 'q':
        break

    number_of_songs = int(songs)

    album = make_album(artist, title, number_of_songs)
    print(f"Created album dictionary: {album}")
