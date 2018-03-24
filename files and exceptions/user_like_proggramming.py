filename =  'user_reasons_like_programming.txt'

prompt = "\nPlease enter, why you like programming?: "
prompt += "\nEnter the 'quit' to end the order!"
message = ""

while message != 'quit':
    with open(filename, 'w') as file_object:
        message = input(prompt)
        file_object.write(print(message))