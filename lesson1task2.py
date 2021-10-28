cube_list = []
temp = 0
sum_divide_seven = 0
sum_remains = 0
number = 1
a = 0
while number <= 1000:
    if number % 2 == 1:
        cube_list.append(number**3)
        a += 1
    number += 1
print(cube_list)
for i in range(len(cube_list)):
    temp = cube_list[i]
    while temp != 0:
        sum_remains += temp % 10
        temp = temp // 10
    if sum_remains % 7 == 0:
        sum_divide_seven += cube_list[i]

    sum_remains = 0
print(sum_divide_seven)
for i in range(len(cube_list)):
    cube_list[i] += 17
    temp = cube_list[i]
    while temp != 0:
        sum_remains += temp % 10
        temp = temp // 10
    if sum_remains % 7 == 0:
        sum_divide_seven += cube_list[i]
    sum_remains = 0
print(sum_divide_seven)