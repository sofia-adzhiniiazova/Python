# 1.Светофор

import time


class TrafficLight:
    __color = ["Красный", "Желтый", "Зеленый"]

    def running(self):
        while True:
            print(self.__color[0])
            time.sleep(7)

            print(self.__color[1])
            time.sleep(2)

            print(self.__color[2])
            time.sleep(5)


result = TrafficLight()
result.running()


# 2.Расчет массы асфальта, необходимого для покрытия всего дорожного полотна.


class Road():
    _length: float
    _width: float

    def __init__(self, length=0, width=0):
        self._length = length
        self._width = width

    def result(self):
        massa = float(input("Введите массу асфальта в кг: "))
        thickness = float(input("Введите толщину полотна в см: "))
        return print(f"Масса асфальта, необходимого для покрытия всего дорожного полотна равна " + str(
            self._length * self._width * massa * thickness / 1000) + "тонн")


total_road = Road(20, 5000)
total_road.result()


# 3.Метод получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).


class Worker:
    name: str
    surname: str
    position: str
    wage: float
    bonus: float
    __income: dict

    def __init__(self, name, surname, position, wage: float = 0, bonus: float = 0):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        self.__income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"Полное имя сотрудника:  {self.name} {self.surname}"

    def get_total_income(self):
        return f"Доход с учетом премии:  {(self.wage + self.bonus)}"


employer_1 = Position('Иван', 'Иванов', 'Менеджер', 50000, 5000)
print(employer_1.get_full_name())
print(employer_1.position)
print(employer_1.get_total_income())

employer_2 = Position('Мария', 'Петрова', 'Инженер', 55000, 10000)
print(employer_2.get_full_name())
print(employer_2.position)
print(employer_2.get_total_income())


# 4. Определение атрибутов машин,вызов методов

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def turn_left(self):
        return f'{self.name} повернула налево'

    def show_speed(self):
        return f'Текущая скорость {self.name} равна  {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость городской машины {self.name} равна {self.speed}')

        if self.speed > 60:
            return f'Скорость {self.name} выше положенной'
        else:
            return f'Скорость {self.name} в пределах допустимой нормы'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость рабочей машины {self.name} равна {self.speed}')

        if self.speed > 40:
            return f'Скорость {self.name} выше положенной'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} это полицейская машина'
        else:
            return f'{self.name} это не полицейская машина'


merc = SportCar(120, 'Белый', 'Mercedes', False)
mini = TownCar(50, 'Зеленый', 'MiniCooper', False)
ford = WorkCar(70, 'Черный', 'Ford', True)
kia = PoliceCar(150, 'Синий', 'Kia', True)
print(merc.turn_left())
print(mini.show_speed())
print(mini.go())
print(ford.show_speed())
print(kia.police())
print(kia.stop())
print(kia.show_speed())


# 5.Канцелярские принадлежности - Запуск отрисовки

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print(f'Отрисовка ручкой {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Отрисовка карандашом {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Отрисовка маркером {self.title}')


pic = Stationery()
pic.draw()
pen = Pen('дома')
pen.draw()
pencil = Pencil('портрета')
pencil.draw()
handle = Handle('на доске')
handle.draw()
