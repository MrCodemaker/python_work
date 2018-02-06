prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quite':
        active = False
    else:
        print(message)

"""
Переменной active присваивается True, чтобы программа начинала работу
в активном состоянии. Это присваивание упрощает команду while,
потому что в самой команде while никакие сравнения не выполняются;
вся логика реализуется в других частях программы.
Пока переменная active остается равной True, цикл выполняется.
В команде if внутри цикла while значение message проверяется после того,
как пользователь введет данные.
Если пользователь ввел строку 'quit', флаг active переходит в состояние False,
а цикл while останавливается. Если пользователь ввел любой текст, кроме 'quit',
то введенные им данные выводятся как сообщение.
"""
