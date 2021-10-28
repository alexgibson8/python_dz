cycle = 1
number = 1
while number <= 100:
    if cycle == 11:
        cycle = 1
        continue
    if number>10 and number<15:
        print (number, "процентов")
    elif cycle == 1:
        print (number, "процент")
    elif cycle>1 and cycle<5:
        print(number, "процента")
    else:
        print(number, "процентов")
    number += 1
    cycle += 1
