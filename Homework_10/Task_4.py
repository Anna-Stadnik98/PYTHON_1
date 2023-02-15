"""
Задание 4.
Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).
Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

words = ['разработка', 'администрирование', 'protocol', 'standard']
for word in words:
    encode_word = word.encode()
    decode_word = encode_word.decode()
    print(f'Начальное слово - "{word}"\nencode - {encode_word}\ndecode - {decode_word}')
