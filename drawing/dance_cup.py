import math
n = int(input()) # 6...100

end_range = n + 1

dots = n
pounds = 3 * n

for row in range(end_range):
    if row > n / 2:
        inner_dots = pounds - 2
        print('.' * dots + '#' + '.' * inner_dots + '#' + '.' * dots)
    else:
        print('.' * dots + '#' * pounds + '.' * dots)
    dots += 1
    pounds -= 2

dots = ((5 * n) - n) / 2
pounds = n
print('.' * int(dots) + '#' * pounds + '.' * int(dots))

bottom_range = n + 2

dots = 2 * n - 2
pounds = (5 * n) - 2 * dots
middle_row = round(n / 2)

for row in range(bottom_range):
    if row == middle_row:
        middle = 'D^A^N^C^E^'
        middle_dots = ((5 * n) - len(middle)) / 2
        if n % 2 == 0:
            print('.' * int(middle_dots) + middle + '.' * int(middle_dots))
        else:
            print('.' * int(middle_dots) + middle + '.' * int(middle_dots) + '.')
    print('.' * int(dots) + '#' * pounds + '.' * int(dots))



