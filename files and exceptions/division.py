try:
print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")

"""
Если бы за кодом try-except следовал другой код, то выполнение программы 
продолжилось, потому что мы объяснили Python, как обрабатывать эту ошибку. 
В следующем примере обработка ошибки позволяет программе продолжить выполнение.
"""