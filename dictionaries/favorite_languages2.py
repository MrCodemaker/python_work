favorite_languages = {
    'edward': 'ruby',
    'phil': 'python',
    'sarah': 'c',
    'sam': 'c++',
    'jason': 'python',
    'jen': 'python',
    'patek': 'swift',
    'eliot': 'perl',
}

were_interviewed = ['jen', 'sarah', 'edward', 'phil']
do_not_were_interviewed = ['sam', 'jason', 'patek', 'eliot']

for name in set(favorite_languages.keys()):
    print(name.title())
    if name in were_interviewed:
        print("Thank you " +
        name.title() +
        " for taking our survey!")
    if name in do_not_were_interviewed:
        print("Dear " +
        name.title() +
        ", please go, our survey!")
