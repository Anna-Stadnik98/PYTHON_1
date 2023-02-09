"""
Задание 4.
Реализуйте базовый класс Car. У данного класса должны быть следующие публичные атрибуты: speed, color, name, is_police (булево). А также публичные методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс публичный метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости. Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        print(f'Cкорость автомобиля {self.speed}')

    def go(self):
        print(f'Автомобиль {self.name} начал движение')

    def stop(self):
        print(f'Автомобиль {self.name} остановился')

    def turn(self, direction):
        print(f'{self.name} повернул {direction}')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'Скорость превышена на {self.speed - 60}')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f'Скорость превышена на {self.speed - 40}! ')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


town_car = TownCar(70, 'синий', 'Kia Rio', False)
town_car.go()
town_car.show_speed()
town_car.turn('налево')
town_car.stop()

sport_car = SportCar(110, 'черный', 'BMW', False)
sport_car.go()
sport_car.show_speed()
sport_car.turn('направо')
sport_car.stop()

work_car = WorkCar(50, 'желтый', 'ГАЗЕЛЬ', False)
work_car.go()
work_car.show_speed()
work_car.turn('направо')
work_car.stop()

police_car = PoliceCar(100, 'серый', 'Ford Focus', True)
police_car.go()
police_car.show_speed()
police_car.turn('налево')
police_car.stop()