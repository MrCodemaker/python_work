sjobs = {'first': 'steve', 'last': 'jobs', 'location': 'california'}
swoz = {'first': 'steve', 'last': 'wozniak', 'location': 'california'}
bgates = {'first': 'bill', 'last': 'gates', 'location': 'washington'}

people = [sjobs, swoz, bgates]

for username, user_info in people.items():
    print("\nUser name: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
