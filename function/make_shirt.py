def make_shirt(size, print_name):
    print("I have a T-shirt with size " + size.upper()
    + " and with a print " + print_name + ".")

make_shirt('s', '"I love HTML"')
make_shirt(size = 'xxl', print_name = '"Hello my Python team!"')

def make_shirt(print_name = '"I love Python"', size = 'l'):
    print("I have a T-shirt with size " + size.upper()
    + " and with a print " + print_name + ".")

make_shirt()
make_shirt('"Hello world"', 'm')
