"""
Задание 3.
Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список только числами.
Класс-исключение должен контролировать типы данных элементов списка.
"""

class NotNumber(Exception):
    def __init__(self, lst):
        self.lst = lst

validations = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', ',')

user_values = input('Введите несколько чисел через пробел: ').split()
numbers = []
for value in user_values:
    try:
        for i in range(len(value)):
            if not (value[i] in validations):
                raise NotNumber(f'{value} - не число')
        numbers.append(float(value))
    except NotNumber as err:
        print(err)

print(f'Числовой массив: {numbers}')
