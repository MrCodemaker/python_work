filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

"""
Аргумент 'a' используется для открытия файла в режиме присоединения 
(вместо перезаписи существующего файла). В точке  записываются две 
новые строки, которые добавляются к содержимому programming.txt
"""
