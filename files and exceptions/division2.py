"""
Правильная обработка ошибок особенно важна в том случае, если программа должна 
продолжить работу после возникновения ошибки. Такая ситуация часто встречается 
в программах, запрашивающих данные у пользователя. Если программа правильно 
среагировала на некорректный ввод, она может запросить новые данные после сбоя. 

Создадим простой калькулятор, который выполняет только операцию деления:
"""

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(answer)