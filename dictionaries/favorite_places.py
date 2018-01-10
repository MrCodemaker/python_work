favorite_places = {
    'elliot': ['new-york'],
    'jane': ['london', 'bangkok'],
    'jason': ['paris',]
    'cornelia': ['moscow', 'saint-petersburg', 'izhevsk']
    }

for name, places in favorite_places.items():
    print("\n" + name.title() + "'s favorite places are:")
    for place in places:
        print("\t" + place.title())
