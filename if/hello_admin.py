users = ['mike', 'ELLIOT', 'admin', 'Alice', 'Sara']

for user in users:
    if user == 'admin':
        print("Hello " + user.title() + ", would you like to see a status report?")
    elif user == 'ELLIOT':
        print("Hello " + user.lower() + ", thank you for loggin again!")
    else:
        print("Hello " + user.title() + ", thank you for loggin again!")
