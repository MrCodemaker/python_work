with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

# or

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

"""
 Метод rstrip() удаляет все пропуски в конце строки. Теперь вывод точно 
 соответствует содержимому исходного файла. 
"""