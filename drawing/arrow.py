import math
n = int(input()) # [3 … 79] n is odd

width = 2 * n - 1
pounds = ''
dots = n // 2

for row in range(n - 1):
    if row == 0:
        pounds = n
        print('.' * dots + '#' * pounds + '.' * dots)
    else:
        inner_dots = width - (dots + 2 + dots)
        print('.' * dots + '#' + '.' * inner_dots + '#' + '.' * dots)

pounds = math.ceil(n / 2)
dots = width - 2 * pounds
print('#' * pounds + '.' * dots + '#' * pounds)

for row in range(1, n):
    dots = row
    inner_dots = width - (2 * dots + 2)
    if row == n - 1:
        print('.' * dots + '#' + '.' * dots)
    else:
        print('.' * dots + '#' + '.' * inner_dots + '#' + '.' * dots)



