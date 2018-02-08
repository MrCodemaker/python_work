def describe_pet(pet_name, animal_type = 'dog'):
    """Выводит информацию о животном."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name = 'willie')

# or

describe_pet('willie')

"""
Мы изменили определение describe_pet() и включили для параметра animal_type
значение по умолчанию 'dog'. Если теперь функция будет вызвана без указания
animal_type, Python знает, что для этого параметра следует использовать
значение 'dog':

I have a dog.
My dog's name is Willie.
"""
