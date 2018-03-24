filename = "guest.txt"

prompt = "What is yor name?"

with open(filename, 'w') as file_object:
    message(input(prompt))
    file_object.write(print(message))
