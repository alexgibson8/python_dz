class Clothes:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_c_size(self):
        return self.width / 6.5 + 0.5

    def get_j_size(self):
        return self.height * 2 + 0.3

    @property
    def get_sq_full(self):
        result = round((self.width / 6.5 + 0.5) + (self.height * 2 + 0.3))
        return str(f'Площадь общая ткани \n'
                   f' {result}')


class Coat(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.get_c_size = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Размер пальто: {self.get_c_size}'


class Jacket(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.get_j_size = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Размер костюма: {self.get_j_size}'


coat = Coat(20, 50)
jacket = Jacket(26, 76)
print(coat)
print(jacket)
print(coat.get_sq_full)
print(jacket.get_sq_full)
