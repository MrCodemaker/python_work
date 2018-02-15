def make_pizza(*toppings):
    """Вывод списка заказанных дополнений."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

"""
Звездочка в имени параметра *toppings приказывает Python создать пустой
кортеж с именем toppings и упаковать в него все полученные значения.
Результат команды print в теле функции показывает, что Python успешно
справляется и с вызовом функции с одним значением, и с вызовом
с тремя значениями. Разные вызовы обрабатываются похожим образом. 
"""
