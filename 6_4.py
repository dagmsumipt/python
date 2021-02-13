class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина начинает движение')

    def stop(self):
         print('Машина остановилась')

    def turn_direction(self, direction):
        print(f'Поворот {direction}')

    def show_speed(self, speed):
        self.speed = speed
        print()

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости')

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости')

class SportCar(Car):
    def auto_type(self):
        print('SportCar')

class PoliceCar(Car):
    def auto_type(self):
        print('PoliceCar')

tc = TownCar(40, 'brown', 'Audi', False)
tc.show_speed()
tc.turn_direction('Направо')