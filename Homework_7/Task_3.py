"""
Задание 3.
Реализовать базовый класс Worker (работник), в котором определить публичные атрибуты name, surname, position (должность), и защищенный атрибут income (доход). Последний атрибут должен ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        print(f'Доход: {self._income["wage"] + self._income["bonus"]}')


work1 = Position('Светлана', 'Петрова', 'бухгалтер', 30000, 15000)
work2 = Position('Татьяна', 'Сидорова', 'секретарь', 20000, 10000)
work1.get_full_name()
work1.get_total_income()
work2.get_full_name()
work2.get_total_income()