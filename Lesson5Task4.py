src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


def nums():
    for i in range(2, len(src)):
        if src[i] > src[i - 1]:
            yield src[i]


temp = nums()
print(next(temp))
print(next(temp))
print(next(temp))
print(next(temp))
print(next(temp))
print(next(temp))
