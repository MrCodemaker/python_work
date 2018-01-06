rivers = {
'volga': 'russia',
'nile': 'egypt',
'hay': 'france',
}

for river, country in set(rivers.items()):
    print("\nThe " + river.title() +
        " runs through " + country.title() +
        "."
        )

for river in set(rivers.keys()):
    print(river.title())

for country in set(rivers.values()):
    print(country.title())
