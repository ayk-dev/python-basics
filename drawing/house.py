n = int(input())

end_range = (n + 1) // 2
star = 1

for row in range(1, end_range + 1):
    if n % 2 == 0:
        print('-' * (end_range - row) + '*' + '*' * star + '-' * (end_range - row))

    else:
        print('-' * (end_range - row) + '*' * star + '-' * (end_range - row))

    star += 2

end_range_second = n // 2
for row in range(1, end_range_second + 1):
    print('|' + '*' * (n - 2) + '|')
