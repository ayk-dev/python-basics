n = int(input())

dots = n + 1
underscore = 2 * n + 1
total_length = dots + underscore + dots
print('.' * dots + '_' * underscore + '.' * dots)

dots = n
underscore = 2 * n - 1
for row in range(1, n + 1):
    print('.' * dots + '//' + '_' * underscore + '\\\\' + '.' * dots)
    dots -= 1
    underscore += 2

sign = 'STOP!'
mid_score = (total_length - 9) // 2
print('//' + mid_score * '_' + sign + '_' * mid_score + '\\\\')


underscore = 4 * n - 1
for row in range(n):
    dots = row
    print('.' * dots + '\\\\' + underscore * '_' + '//' + dots * '.')
    underscore -= 2