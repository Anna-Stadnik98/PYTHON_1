"""
Задание 2.
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

class DivisionByNull(Exception):

    def __init__(self, division):
        self.division = division


num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))

try:
    if num2 == 0:
        raise DivisionByNull('Деление на ноль недопустимо!')
    res = num1 / num2
except DivisionByNull as err:
    print(err)
else:
    print(f'Результат: {res}')