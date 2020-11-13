n = int(input())
# ширина 2 * n - 1 колони
# height 2 * (n - 2) + 1
# Лявата и дясната ѝ част са широки n - 1

middle = n - 1
s = (n - 1) - 1
dash = ''
r = 2 * (n - 2) + 1 # range = height
spaces = n - 1

for row in range(1, r + 1):
    if row == middle:
        print(' ' * spaces + '@' + ' ' * spaces)
    elif row < middle:
        if row % 2 != 0:
            print('*' * s + '\\' + ' ' + '/' + '*' * s)
        elif row % 2 == 0:
            print('-' * s + '\\' + ' ' + '/' + '-' * s)
    else:
        if row % 2 != 0:
            print('*' * s + '/' + ' ' + '\\' + '*' * s)
        elif row % 2 == 0:
            print('-' * s + '/' + ' ' + '\\' + '-' * s)



