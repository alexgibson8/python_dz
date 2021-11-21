def type_longer(callback):
    def wrapper(*args):
        for i in args:
            print(i, type(i))
        result = callback(*args)
        return result

    return wrapper


@type_longer
def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


@type_longer
def square(x):
    return x ** 2


print(addition(2, 3))
print(subtraction(3, 2))
print(square(2))
