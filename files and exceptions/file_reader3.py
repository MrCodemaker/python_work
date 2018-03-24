# Для последовательной обработки каждой строки в файле можно воспользоваться
# циклом for:

filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())