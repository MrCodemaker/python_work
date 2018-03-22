filename = 'pi_digits.txt'

with open as file_object:
lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

"""
ПРИМЕЧАНИЕ 
Читая данные из текстового файла, Python интерпретирует весь текст в 
файле как строку . Если вы читаете из текстового файла число и хотите 
работать с ним в числовом контексте, преобразуйте его в целое число 
функцией int() или в вещественное число функцией float() .

"""