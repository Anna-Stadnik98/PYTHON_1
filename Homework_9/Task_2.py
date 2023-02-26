"""
Задание 2.
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

class ZeroDivideException(Exception):
    def __init__(self, msg):
        self.msg = msg


number1 = int(input('Введите число 1: '))
number2 = int(input('Введите число 2: '))

try:
    if number2 == 0:
        raise ZeroDivideException('Делить на ноль нельзя')
    print(f'{number1} : {number2} = {number1 / number2}')
except ZeroDivideException as err:
    print(err)
