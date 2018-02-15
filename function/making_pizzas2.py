from pizza_modul import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

"""
При таком синтаксисе использовать точечную запись (имя_модуля.имя_функции())
при вызове функции не обязательно. Так как функция make_pizza() явно
импортируется в команде import, при использовании её можно вызывать
прямо по имени.
"""
