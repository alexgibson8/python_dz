class Divide(Exception):
    def __init__(self, txt):
        self.txt = txt

def div_0():
    try:
        num_1 = int(input('Введите делимое: '))
        num_2 = int(input('Введите делитель: '))
        if num_2 == 0:
            raise Divide('Делить на ноль нельзя!')
        else:
            result = num_1 / num_2
            return result
    except ValueError:
        return "Вы ввели не число"
    except Divide as err:
        return err
print(div_0())