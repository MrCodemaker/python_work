def build_car(brand, model, **car_info):
    car = {}
    car['car_brand'] = brand
    car['car_model'] = model
    for key, value in car_info.items():
        car[key] = value
    return car

car_description = build_car('subaru', 'outback',
                            color = 'blue', tow_package = True)
print(car_description)
