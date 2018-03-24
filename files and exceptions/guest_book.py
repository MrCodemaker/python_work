filename =  'guest_book.txt'

prompt = "\nPlease enter the name of the supplement: "
prompt += "\nEnter the 'quit' to end the order!"
message = ""

while message != 'quit':
    with open(filename, 'w') as file_object:
        message = input(prompt)
        file_object.write(print(message))
    
 