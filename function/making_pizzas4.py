"""
Псевдоним также можно назначить для всего модуля. Назначение короткого
имени для модуля — скажем, p_m для pizza_modul — позволит вам быстрее вызывать
функции модуля. Вызов p_m.make_pizza() получается более компактным, чем
pizza_modul.make_pizza():
"""

import pizza_modul as p_m

p_m.make_pizza(16, 'pepperoni')
p_m.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#Общий синтаксис выглядит так:
# import имя_модуля as псевдоним
 
