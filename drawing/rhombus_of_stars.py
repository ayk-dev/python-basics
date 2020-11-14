n = int(input())

#for row in range(1, n + 1):
####print(' ' * (n - row) + '* ' * row)

#for row in range(1, n):
####print(' ' * row + '* ' * (n - row))

space = ' '
star = '* '
for row in range(1, 2 * n):
    if row <= n:
        print(space * (n - row) + star * row)
    else:
        print(space * (row - n) + star * (2 * n - row))

