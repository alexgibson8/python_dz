tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Станислав', 'Егор']
klass = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def class_info():
    if len(tutors) > len(klass):
        for i in range(len(klass), len(tutors)):
            klass.append('None')
    print(klass)
    for i in range(len(tutors)):
        t = tutors[i], klass[i]
        result = tuple(t)
        yield result


temp = class_info()
print(next(temp))
print(next(temp))
print(next(temp))
print(next(temp))
print(next(temp))
print(next(temp))
print(next(temp))
print(next(temp))
print(next(temp))
