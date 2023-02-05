"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""

arg1 = int(input('Введите первое число: '))
arg2 = int(input('Введите второе число: '))
arg3 = int(input('Введите второе число: '))

def my_func2(*args):
    list = []
    list.append(arg1)
    list.append(arg2)
    list.append(arg3)
    list.sort(reverse=True)    
    return list[0] + list[1]
   
print(f'Решение с функцией sort: {my_func2()}')

def my_func(*args):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3
    
print(f'Решение без функции sort: {my_func()}')