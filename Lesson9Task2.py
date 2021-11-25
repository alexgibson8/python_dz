class Road:
    def __init__(self, _length, _width, _weight, _high):
        self._length = _length
        self._width = _width
        self._weight = _weight
        self._high = _high
        self.result = (_width * _length * _high * _weight) // 1000


road_1 = Road(20, 5000, 25, 5)
print(road_1.result, 'тон')
