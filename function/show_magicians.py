def show_magicians(magicians):
    for magician in magicians:
        message = "Hello, " + magician.title() + "!"
        print(message)
magician_names = ['mike', 'john', 'kane']

show_magicians(magician_names)

def make_great(magicians):
    for magician in magicians:
        message = "Hello, " + magician.title() + "!"
        print(message)
magician_names = ['great mike', 'great john', 'great kane']

show_magicians(magician_names)

make_great(magician_names[:])
