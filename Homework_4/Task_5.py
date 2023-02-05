"""
5. Сделайте профилирование кода любого или любых выполненных заданий
с помощью модуля timeit, опишите результат
"""

from timeit import timeit

x = int(input('Введите действительное положительное число: '))
y = int(input('Введите целое отрицательное число: '))

def my_func(x, y):
    v1 = x ** y
    v2 = 1
    i = 1
    while i <= abs(y):
        v2 *= x
        i += 1

    return 1 / v2

print(my_func(x, y))

def my_func2(x, y):
    return x ** y

print(my_func2(x, y))    

print(timeit('my_func', globals=globals(), number=100000))
print(timeit('my_func2', globals=globals(), number=100000))

"""
Использование встроенной функции снижает время.
"""