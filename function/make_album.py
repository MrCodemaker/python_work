def get_album(musician_name, album_name, number_of_tracks = ''):
    album_info = {'musician': musician_name, 'album': album_name}
    if number_of_tracks:
        album_info['number_of_tracks'] = number_of_tracks
    return album_info

album = get_album('justin timberlake', 'man of the woods')
print(album)

album = get_album('lana del rey', 'honeymoon')
print(album)

album = get_album('vince staples', 'hell can wait', number_of_tracks = 7)
print(album)

album = get_album('everything was beautiful, and nothing hurt', 'moby')
print(album)
