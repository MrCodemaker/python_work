def get_formatted_location(city_name, country_name):
    full_name = city_name + ' ' + country_name
    return full_name.title()
location = get_formatted_location('london', 'britain')
print(location)

location = get_formatted_location('izhevsk', 'russia')
print(location)

location = get_formatted_location('stockholm', 'sweden')
print(location)
