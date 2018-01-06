favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("Sarah's favorite language is " +
    favorite_languages['sarah'].title() +
    ".")

# or

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")

# or

# Перебор всех ключей в словаре с помощью метода .keys()

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in favorite_languages.keys():
    print(name.title())

"""
Или же можно опустить метод .keys(), так как без него код будет работать
точно также
"""

# or

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(" Hi " + name.title() +
            ", I see your favorite language is " +
            favorite_languages[name].title() + "!")

# or

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

#or

# Получение упорядоченной копии ключей можно воспользоваться функцией sorted()!

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

"""
Python выдаст список ключей в словаре и отсортирует его перед тем, как
переберёт элементы.
"""

# or

# Перебор всех значений в словаре с помощью метода .value()

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# or

"""
Значения извлекаются из словаря без проверки на возможные повторения.
Для небольших словарей это может быть приемлемо, но в опросах с большим
количеством респондентов список будет содержать слишком много дубликатов.
Чтобы получить список выбранных языков без повторений, можно воспользоваться
множеством (set). Множество в целом похоже на список, но все его элементы
должны быть уникальными:
"""

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
