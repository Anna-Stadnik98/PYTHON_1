"""
Задание 7. Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.
Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2
Нужно написать рекурсивную ф-цию только для левой части выражения!
Результат нужно сверить с правой частью.
Правой части выражения в рекурсивной ф-ции быть не должно!
Решите через рекурсию. В задании нельзя применять циклы.
"""

def input_number():
    try:
        number = int(input('Введите любое натуральное число '))
        if number > 0:
            return number
    except Exception as e:
        pass
    print('Введено некорректное значение.')
    return input_number()

def sum(end, result = 0, current = 1):
    result += current
    current += 1
    if current > end:
        return result
    return sum(end, result, current)
   
end = input_number()
left_resutl = sum(end)
right_result = end*(end + 1)/2

if left_resutl == right_result:
    print(f'1+2+...+n = {left_resutl}\nn(n+1)/2 = {int(right_result)}\n1+2+...+n = n(n+1)/2 для n = {end} истинно')
else:
    print('Так быть не может')