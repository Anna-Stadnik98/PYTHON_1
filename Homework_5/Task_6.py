"""
Задание 6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. В задании нельзя применять циклы.
"""

import random

def input_number():
    try:
        number = int(input('Введите число от 0 до 100: '))
        if number >= 0 and number <= 100:
            return number
    except Exception as e:
        pass
    print('Введено некорректное значение.')
    return input_number()
    
def check_customer_number(true_number, customer_number):
    if true_number == customer_number:
        print('Вы угадали!')
        return True
    elif customer_number > true_number:
        print('Ваше число больше, чем загаданное.')
    else:
        print('Ваше число меньше, чем загаданное.')
    return False

def guess_process(current_number, count_attempt):
    if count_attempt == 0:
        print(f'Закончились попытки, загаданное число: {current_number}')
        return
    customer_number = input_number()
    if check_customer_number(current_number, customer_number):
        return
    count_attempt -= 1
    guess_process(current_number, count_attempt)

print('Отгадайте число!')
guess_process(random.randint(0, 100), 10)