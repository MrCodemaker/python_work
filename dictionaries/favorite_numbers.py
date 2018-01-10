favorite_numbers = {
    'eric': [2, 55]
    'eliot': [1, 4, 89]
    'sarah': [23, 1, 13, 5]
    'alice': [3]
    'james': [5, 25]
    }

for name, numbers in set(favorite_numbers.items()):
    print("\n" + name.title() + "'s favorite numbers are: ")
    for number in numbers:
        print("\t" + number.title())    
