filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

"""
Метод readlines() последовательно читает каждую строку из файла и сохраняет ее 
в списке. Список сохраняется в переменной lines, с которой можно продолжить 
работу после завершения блока with. В простом цикле for выводятся все элементы 
списка lines. Так как каждый элемент lines соответствует ровно одной 
строке файла, вывод точно соответствует его содержимому.
"""