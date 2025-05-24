def make_album(artist_name, album_title, number_of_songs=None):
    album = {
        "artist": artist_name,
        "title": album_title
    }
    if number_of_songs is not None:
        album["songs"] = number_of_songs
    return album

album1 = make_album("James","Kobita")
album2 = make_album("Arnob","Tomar jonno")
album3 = make_album("Tahsan","Alo","80")
                    
print(album1)
print(album2)
print(album3)