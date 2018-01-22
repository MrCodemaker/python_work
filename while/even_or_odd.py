"""
Оператор % не сообщает частное от целочисленного деления; он возвращает только
остаток. Когда одно число нацело делится на другое, остаток равен 0,
и оператор % возвращает 0. Например, этот факт может использоваться
для проверки четности или нечетности числа:
"""

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")

"""
Четные числа всегда делятся на 2. Следовательно,
если остаток от деления на 2 равен 0 (number % 2 == 0), число четное,
а если нет — нечетное.

Enter a number, and I'll tell you if it's even or odd: 42
The number 42 is even.
"""
