class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):
    def get_full_name(self):
        print(self.name + ' ' + self.surname)

    def get_total_income(self):
        print(self._income['wage'] + self._income['bonus'])

w = Position('Dmitrii', 'Gerasimov', 'analyst', {'wage': 4000, 'bonus': 1000})
w.get_full_name()
w.get_total_income()
