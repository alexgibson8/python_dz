import sys
from sys import argv

sales = sys.argv[1]
with open('bakery.csv', 'a', encoding='utf-8') as f_1:
    print(sales, file=f_1)

with open('bakery.csv', 'r', encoding='utf-8') as f_2:
    p = len(argv)
    if p == 1:
        print(f_2.read)
    elif p == 2:
        for lines in f_2.readlines()[int(argv[1]) - 1:]:
            print(lines, end='')
    elif p == 3:
        i = 0
        for lines in f_2:
            i += 1
            if i >= int(argv[1]):
                if i > int(argv[2]):
                    break
                print(lines, end='')
