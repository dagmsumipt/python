import time
import sys
class TrafficLights():
    def __init__(self, color):
        self._color = color


    def running(self):
        if self._color == 'красный':
            print('Красный')
            print('Горит 7 сек')
            time.sleep(10)
        else:
            print('Неправильный порядок')
            sys.exit()
        print('Желтый')
        print('Горит 5 сек')
        time.sleep(5)
        print('Зеленый')
        print('Горит 15 сек')
        time.sleep(15)

tl = TrafficLights('красный')
tl.running()