filename = 'pi_million_digits.txt'

with open as file_object:
line = file_object.readlines()

pi_string = ''
for line in lines:
pi_string += line.rstrip()

birthday = input("Enter you birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
