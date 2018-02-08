def describe_city(city_name, country_name = 'russia'):
    print(city_name.title() + " is in " + country_name.title())

describe_city('izhevsk')
describe_city(city_name = 'london')
describe_city(city_name = 'edinburg', country_name = 'scotland')
