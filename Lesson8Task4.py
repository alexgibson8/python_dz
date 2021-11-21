def val_checker(callback):
    def wrapper(*args):
        wrong_number = 0
        for i in args:
            if int(i) < 0:
                wrong_number += 1
        if wrong_number == 0:
            result = callback(*args)
            return result
        else:
            raise ValueError(f'wrong numbers: {args}')
    return wrapper


@val_checker
def square(x,y):
    return x*y

@val_checker
def cube(x):
    return x ** 3


print(square(-2,3))
print(cube(-5))


