a = '\"'  # элемент, который необходимо вставить по условию
i = 0
check_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'радусов']  # список слов
while i < len(check_list):
    if check_list[i] == '5':  # проверка слов на наличие символа "5"
        check_list[i] = '05'
        check_list.insert(i, a)
        check_list.insert(i + 2, a)
        i += 2
    elif check_list[i] == '17':  # проверка слов на наличие символа "17"
        check_list.insert(i, a)
        check_list.insert(i + 2, a)
        i += 2
    elif check_list[i] == '+5':  # проверка слов на наличие символа "+5"
        check_list[i] = '+05'
        check_list.insert(i, a)
        check_list.insert(i + 2, a)
        i += 2
    else:
        i += 1  # во всех остальных случаях просто проходим дальше по кортежу
print(check_list)  # вывод кортежа
print(check_list[0] + ' ' + '"' + check_list[2] + '"' + ' ' + check_list[4] + ' ' + '"' + check_list[6] + '"' + ' ' +
      check_list[8] + ' ' + check_list[9] + ' ' + check_list[10] + ' ' + check_list[11] + ' ' + '"' + check_list[
          13] + '"' + ' ' + check_list[15])  # вывод нужной строки
