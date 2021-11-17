users = {}
with open('users.csv', 'r', encoding='utf-8') as f_1, \
        open('hobby.csv', 'r', encoding='utf-8') as f_2, \
        open('users.txt', 'w', encoding='utf-8') as f_3:
    for line_1 in f_1:
        line_2 = f_2.readline().strip()
        if not line_2:
            line_2 = None
        f_3.write(f'{line_1.strip()} : {line_2}\n')
