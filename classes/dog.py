class Dog():
    """Простая модель собаки."""

    def _init_(self, name, age):
        """Инициализирует атрибуты name и age."""
        self.name = name
        self.age = age

    def sit(self):
        """Собака садится по команде."""
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
        """Собака перекатывается по команде."""
        print(self.name.title() + " rolled over!")


my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

"""
Для обращения к атрибутам экземпляра используется «точечная» запись.
Мы обращаемся к значению атрибута name экземпляра my_dog:

my_dog.name

Точечная запись часто используется в Python. Этот синтаксис показывает,
как Python ищет значения атрибутов. В данном случае Python обращается к
экземпляру my_dog и ищет атрибут name, связанный с экземпляром my_dog.
Это тот же атрибут, который обозначался self.name в классе Dog.
Тот же прием используется для работы с атрибутом age. В первой команде
print вызов my_dog.name. title() записывает 'willie' (значение атрибута name
экземпляра my_dog) с символа верхнего регистра. Во второй команде print вызов
str(my_dog.age) преобразует 6, значение атрибута age экземпляра my_dog,
в строку. Пример выводит сводку известных фактов о my_dog:

My dog's name is Willie.
My dog is 6 years old.

"""
"""
Вызов методов После создания экземпляра на основе класса Dog можно применять
точечную запись для вызова любых методов, определенных в Dog:

my_dog = Dog('willie', 6)
my_dog.sit()
my_dog.roll_over()

Чтобы вызвать метод, укажите экземпляр (в данном случае my_dog) и
вызываемый метод, разделив их точкой. В ходе обработки my_dog.sit() Python
ищет метод sit() в классе Dog и выполняет его код. Строка my_dog.roll_over()
интерпретируется аналогичным образом. Теперь экземпляр послушно выполняет
полученные команды:

Willie is now sitting.
Willie rolled over!

Это очень полезный синтаксис. Если атрибутам и методам были присвоены
содержательные имена (например, name, age, sit() и roll_over()), разработчик
сможет легко понять, что делает блок кода, — даже если он видит этот
блок впервые.
"""

# На основе класса можно создать столько экземпляров, сколько вам потребуется.
# Создадим второй экземпляр Dog с именем your_dog:

my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old."
my_dog.sit()

print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + "years old.")
your_dog.sit()

"""
В этом примере создаются два экземпляра с именами Willie и Lucy.
Каждый экземпляр обладает своим набором атрибутов и способен выполнять
действия из общего набора:

My dog's name is Willie.
My dog is 6 years old.
Willie is now sitting.

Your dog's name is Lucy.
Your dog is 3 years old.
Lucy is now sitting.

Даже если второй собаке будут назначены те же имя и возраст, Python все равно
создаст отдельный экземпляр класса Dog. Вы можете создать сколько угодно
экземпляров одного класса при условии, что эти экземпляры хранятся в переменных
с разными именами или занимают разные позиции в списке или словаре.
"""
