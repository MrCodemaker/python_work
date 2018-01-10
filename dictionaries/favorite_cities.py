cities = {
    'london': {
        'country': 'england',
        'population': 8538689,
        'fact': 'was founded by the Romans',
        },
    'moscow': {
        'country': 'russia',
        'population': 12380664,
        'fact': ' is the largest transport hub of the country.'
        },
    'new-york': {
        'country': 'usa',
        'population': 8405837,
        'fact': [' - the only city in which women are officially allowed to',
        'walk along the street with their naked breasts.']
        },
    }

for city_name, city_info in cities.items():
    print("\nCity name:" + city_name.title())
    print("\t" + city_name.title() +
        " has a population of " +
        city_info['population'] +
        " people!")
    print("\t" + city_name.title() + city_info['fact'])
