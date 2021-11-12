MAX_NUM = 15


def gen_odd_nums():
    for i in range(1, MAX_NUM + 1, 2):
        yield i


temp = gen_odd_nums()
print(next(temp))
print(next(temp))
print(next(temp))
print(next(temp))
print(next(temp))
print(next(temp))
print(next(temp))
print(next(temp))

odd_nums = (nums for nums in range(1, MAX_NUM + 1, 2))
print(next(odd_nums))
print(next(odd_nums))
print(next(odd_nums))
print(next(odd_nums))
print(next(odd_nums))
print(next(odd_nums))
print(next(odd_nums))
print(next(odd_nums))
