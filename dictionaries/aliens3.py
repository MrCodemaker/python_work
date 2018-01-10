# Создание пустого списка для хранения пришельцев.
aliens = []

# Создание 30 зелёных пришельцев.
for alien_number in range(0,30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens(0:3):
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

"""
Цикл можно расширить, добавив блок elif для превращения жёлтых пришельцев
в красных - быстрых и приносящих игроку по 15 очков. Мы не станем приводить
весь код, а цикл выглядит так.

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15 
"""

# Вывод первых 5 пришельцев:
for alien in aliens[0:5]:
print(alien)
print("...")
