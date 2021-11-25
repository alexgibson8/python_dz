class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки картины {self.title} (ручка)')


class Pensil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки картины {self.title} (карандаш)')


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки картины {self.title} (маркер)')


pic_1 = Stationery('Мона Лиза')
pic_1.draw()
pic_2 = Pen('Опять двойка')
pic_2.draw()
pic_3 = Pensil('Черный квадрат')
pic_3.draw()
pic_4 = Handle('Утро в сосновом бору')
pic_4.draw()
