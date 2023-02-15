"""
Задание 5.
Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.
Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess
import chardet

url_list = ['yandex.ru', 'youtube.ru']

for url in url_list:
    ping = subprocess.Popen(['ping', url], stdout=subprocess.PIPE)
    for line in ping.stdout:
        res = chardet.detect(line)
        line = line.decode(res['encoding'])
        print(line)
