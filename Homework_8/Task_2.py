"""
2) Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open('task_1.txt') as stream:
    data = stream.readlines()
    print(f'Количество строк в файле = {len(data)} ')
    number = 1
    for line in data:
       print(f'Колиечство слов в {number} строке = {len(line.split())}')
       number += 1