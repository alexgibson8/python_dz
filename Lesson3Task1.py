def num_translate_adv(num):
    eng_numbers = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восмь',
        'nine': 'девять',
        'ten': 'десять'
    }
    if num.istitle() and eng_numbers.get(num.lower()):
        return eng_numbers.get(num.lower(), 'None')
    else:
        return eng_numbers.get(num, 'None')


print('Введите число от 0 до 10 на английском')
number = input()
print(num_translate_adv(number))
