def greet_users(names):
    """Вывод простого приветствия в списке."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)
usernames = ['hannah', 'ty', 'margot']

greet_users(usernames)
