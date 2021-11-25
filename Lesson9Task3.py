SALARY = {
    'wage': 10000,
    'bonus': 5000,
}


class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = SALARY['wage']


class Position(Worker):
    def get_full_name(self):
        result = self.name + ' ' + self.surname
        return result

    def get_total_income(self):
        total_income = self.income + SALARY['bonus']
        return total_income


worker_1 = Position('Саша', 'Козлов', 'Сторож')
print(worker_1.get_full_name())
print(worker_1.get_total_income())
