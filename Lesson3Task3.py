def thesaurus(*args):
    args_sorted = sorted(args)
    symbols = dict()
    for name in args_sorted:
        first_letter = name[0]
        if first_letter not in symbols:
            symbols[first_letter] = []
        symbols[first_letter].append(name)
    return symbols


print(thesaurus('Иван', 'Игорь', 'Анастасия', 'Константин', 'Артем'))
