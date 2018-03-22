filename = 'pi_million_digits.txt'

with open(filename) as file_object: 
lines = file_object.readlines() 
pi_string = '' 
for line in lines: 
pi_string += line.strip()    

print(pi_string[:52] + "...") 
print(len(pi_string)) 

"""
Из выходных данных видно, что строка действительно содержит значение «пи» 
с точностью до 1 000 000 знаков: 

3.14159265358979323846264338327950288419716939937510... 
1000002 
"""

"""
ПРИМЕЧАНИЕ 
Для запуска этой программы (и многих других примеров, приведенных ниже) 
необходимо загрузить ресурсы по адресу 
https://www .nostarch .com/pythoncrashcourse/ .
"""