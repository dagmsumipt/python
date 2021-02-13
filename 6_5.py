class Stationery:
    def __init__(self):
        self.title = 'Stationery'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('This is a pen')


class Pencil(Stationery):
    def draw(self):
        print('This is a pencil')


class Handle(Stationery):
    def draw(self):
        print('This is a handle')

s = Stationery()
s.draw()
print(s.title)
p1 = Pen()
p1.draw()
p2 = Pencil()
p2.draw()
h = Handle()
h.draw()
