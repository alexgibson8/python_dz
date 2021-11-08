from random import randrange

nouns = ['автомобиль', 'лес', 'огонь', 'город', 'дом']
adverbs = ['сегодня', 'вчера', 'завтра', 'позавчера', 'ночью']
adjectives = ['веселый', 'яркий', 'зеленый', 'утопичный', 'мягкий']
jokes = []


def get_jokes(num):
    for i in range(num):
        noun = randrange(len(nouns))
        adverb = randrange(len(adverbs))
        adjective = randrange(len(adjectives))
        temp = nouns[noun] + ' ' + adverbs[adverb] + ' ' + adjectives[adjective]
        jokes.append(temp)
        del nouns[noun]
        del adverbs[adverb]
        del adjectives[adjective]
    print(jokes)
    return jokes


number = int(input('Введите число шуток: '))
if number > 5:
    number = 5
    print('Будет выведено 5 шуток, потому что в списке их всего 5')
elif number < 0:
    number = 0
    print('Мы не выведем вам ни одной шутки, так как вы ввели число шуток меньше нуля')
get_jokes(number)
