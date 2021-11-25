class Car:
    def __init__(self, speed, colour, name, is_police):
        self.speed = speed
        self.colour = colour
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} останвилась')

    def turn(self, direction):
        print(f'{self.name} повернула {direction}')

    def show_speed(self):
        print(f'{self.name} движется со скоростью {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} превысила скорость!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name} превысила скорость!')


class PoliceCar(Car):
    def is_police(self):
        if self.is_police == True:
            print('Это полицейская машина!')


TownCar_1 = TownCar(70, 'зеленый', 'Lada', False)
TownCar_1.go()
TownCar_1.turn('направо')
TownCar_1.stop()
TownCar_1.show_speed()
SportCar_1 = SportCar(80, 'красный', 'BMW', False)
SportCar_1.go()
SportCar_1.turn('налево')
SportCar_1.stop()
SportCar_1.show_speed()
WorkCar_1 = WorkCar(50, 'желтый', 'Ford', False)
WorkCar_1.go()
WorkCar_1.turn('направо')
WorkCar_1.stop()
WorkCar_1.show_speed()
PoliceCar_1 = PoliceCar(150, 'черный', 'Lada', True)
PoliceCar_1.go()
PoliceCar_1.turn('направо')
PoliceCar_1.stop()
PoliceCar_1.show_speed()