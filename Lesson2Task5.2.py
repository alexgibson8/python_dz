prices = [6.9, 1.5, 2, 3.4, 5.14, 7, 9.1, 4.07, 10, 11.6, 8.7]  # кортеж с ценами
temp = []  # временный кортеж
expensive = []  # кортеж для самых больших цен
idx = 0
index = 1
for i in range(len(prices)):
    if type(prices[i]) == int:
        prices[i] = float(prices[i])  # все int числа становятся float
    whole_part = int(prices[i] // 1)
    str_whole = str(whole_part) + ' руб'
    temp.append(str_whole)  # ввод целых частей от чисел формата "<> руб"
    if round(prices[i] - whole_part, 2) * 10 == 0:  # ввод дробных частей от чисел формата "<> коп"
        t = '0' + str(int(round(prices[i] - whole_part, 2) * 100)) + ' коп'
        temp.append(t)
    elif round(prices[i] - whole_part, 2) < 0.1:  # ввод дробных частей от чисел формата "<> коп"
        t = '0' + str(int(round(prices[i] - whole_part, 2) * 100)) + ' коп'
        temp.append(t)
    elif round(prices[i] - whole_part, 2) * 10 > 0:  # ввод дробных частей от чисел формата "<> коп"
        t = str(int(round(prices[i] - whole_part, 2) * 100)) + ' коп'
        temp.append(t)
while idx < len(temp):  # вывод кортежа по условию задачи
    print(temp[idx], temp[idx + 1], sep=' ', end=', ')
    idx += 2
print(' ')
print(id(prices), prices)
prices.sort()
print(id(prices), prices)  # вывод отсортированного in-place кортежа
rev_prices = sorted(prices, reverse=True)
print(id(rev_prices), rev_prices)  # вывод развернутного кортежа
for i in range(len(rev_prices)):  # сортировка 5 самых больших цен
    if index < 5:
        expensive.append(rev_prices[i])
    index += 1
expensive.sort()
print(expensive)
