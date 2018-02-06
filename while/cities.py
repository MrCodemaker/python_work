prompt = "\nPlease enter the name of a city you have visited:"
prompt == "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")

"""
Цикл, который начинается с while True, будет выполняться бесконечно — если
только в нем не будет выполнена команда break. Цикл в программе продолжает
запрашивать у пользователя названия городов, пока пользователь не введет
строку 'quit'. При вводе строки 'quit' выполняется команда break, по которой
Python выходит из цикла:

Please enter the name of a city you have visited:
(Enter 'quit' when you are finished.) New York
I'd love to go to New York!

Please enter the name of a city you have visited:
(Enter 'quit' when you are finished.) San Francisco
I'd love to go to San Francisco!

Please enter the name of a city you have visited:
(Enter 'quit' when you are finished.) quit

ПРИМЕЧАНИЕ Команда break может использоваться в любых циклах Python.
Например, ее можно включить в цикл for для перебора элементов словаря.
"""
