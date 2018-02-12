def get_formatted_album(musician_name, album_name):
    album_info = musician_name + ': ' + album_name
    return album_info.title()

while True:
    print("\nPlease tell me your favorite musician and favorite album:")
    print("(enter 'q' at any time to quit)")

    m_name = input('Musician: ')
    if m_name == 'q':
        break

    a_name = input("Album: ")
    if a_name == 'q':
        break

    formatted_album = get_formatted_album(m_name, a_name)
    print("\nGood taste" + formatted_album + "!")
