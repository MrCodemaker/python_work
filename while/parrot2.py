prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

"""
Цикл while выполняется, пока значение message не равно 'quit'.

При первом выполнении цикла message содержит пустую строку,
и Python входит в цикл. При выполнении команды message = input(prompt)
Python отображает подсказку и ожидает, пока пользователь введет данные.
Эти данные сохраняются в message и выводятся командой print;
после этого Python снова проверяет условие команды while.
Пока пользователь не введет слово 'quit', приглашение будет выводиться
снова и снова, а Python будет ожидать новых данных.

При вводе слова 'quit' Python перестает выполнять цикл while,
а программа завершается:

Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. Hello everyone!
Hello everyone!

Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. Hello again.
Hello again.

Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. quit
quit
"""

"""
Программа работает неплохо, если не считать того,
что она выводит слово 'quit', словно оно является обычным сообщением.
Простая проверка if решает проблему:

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
message = input(prompt)

    if message != 'quit':
print(message)

Теперь программа проводит проверку перед выводом сообщения и выводит
сообщение только в том случае, если оно не совпадает с признаком завершения:

Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. Hello everyone!
Hello everyone!

Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. Hello again.
Hello again.

Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. quit
"""
