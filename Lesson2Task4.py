text = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
        'директор аэлита']  # список имен
words = []  # кортеж для внесения в него отдельных слов из кортежа text
names = []  # кортеж для внесения в него имен из кортежа words
for i in range(len(text)):
    words += text[i].split()  # разделение записей кортежа на отдельные слова
print(words)  #
for i in range(len(words)):
    if words[i] == 'Игорь':
        names.append(words[i])  # проверка на имя Игорь
    elif words[i] == 'МАРИНА':
        names.append(words[i].capitalize())  # проверка и исправление на имя Марина
    elif words[i] == 'нИКОЛАй':
        names.append(words[i].capitalize())  # проверка и исправление на имя Николай
    elif words[i] == 'аэлита':
        names.append(words[i].capitalize())  # проверка и исправление на имя Аэлита
print(names)
for i in range(len(names)):
    print('Привет,', names[i] + '!')  # Вывод фразы
