"""
Иногда подсказка занимает более одной строки. Например, вы можете сообщить
пользователю, для чего программа запрашивает данные. Текст подсказки можно
сохранить в переменной и передать эту переменную функции input(): вы строите
длиное приглашение из нескольких строк, а потом выполняете одну компактную
команду input().
"""

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello, " + name + "!")

"""
В этом примере продемонстрирован один из способов построения длинных строк.
Первая часть длинного сообщения сохраняется в переменной prompt. Затем
оператор += объединяет текст, хранящийся в prompt, с новым фрагментом текста.
Теперь содержимое prompt занимает две строки (вопросительный знак снова
отделяется от ввода пробелом):

If you tell us who you are, we can personalize the messages you see.
What is your first name? Eric

Hello, Eric!
"""
