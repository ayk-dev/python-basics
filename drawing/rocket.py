import math
n = int(input())
is_n_even = n % 2 == 0
w = 3 * n # rocket width = 3 * n koloni
# Pravim purvo shapkata ili nosa na raketata

dots = (w - 2) // 2
spaces = ''
if is_n_even:
    spaces = 0
else:
    spaces = 1

for row in range(1, n + 1):
    print(dots * '.' + '/' + spaces * ' ' + '\\' + dots * '.')
    spaces += 2
    dots -= 1

dots = (w - (2 * n)) // 2
stars = ''
if is_n_even:
    stars = 2 * n
else:
    stars = 2 * n + 1
print('.' * dots + stars * '*' + '.' * dots)

backslash = ''
if is_n_even:
    dots = n / 2
    backslash = 2 * n - 2
else:
    dots = n // 2
    backslash = (2 * n - 2) + 1

for row in range(2 * n):
    print('.' * int(dots) + '|' + '\\' * int(backslash) + '|' + '.' * int(dots))

bottom_range = n // 2
dots = n // 2
stars = ''
if is_n_even:
    stars = 3 * n - (n + 2)
else:
    stars = 3 * n - (n + 2) + 1

for row in range(1, bottom_range + 1):
    print('.' * dots + '/' + '*' * stars + '\\' + '.' * dots)
    stars += 2
    dots -= 1

