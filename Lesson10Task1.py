class Matrix:
    def __init__(self, list):
        self.list = list

    def __str__(self):
        return '\n'.join(map(str, self.list))

    def __add__(self, other):
        for i in range(len(self.list)):
            for i_2 in range(len(other.list[i])):
                self.list[i][i_2] = self.list[i][i_2] + other.list[i][i_2]
        return Matrix.__str__(self)


m_1 = Matrix([[-1, 2, 1], [-1, 0, 6], [0, 88, -1], [1, 47, -1]])
new_m = Matrix([[-2, 73, 2], [-2, 7, 2], [0, 2, -2], [46, 2, -7]])
print(m_1.__add__(new_m))