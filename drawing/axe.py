# ---------------**--------
n = int(input()) # 2...42

w = 5 * n
left_dash = 3 * n
inner_dash = 0
right_dash = w - (2 + left_dash + inner_dash)

for row in range(n):

    print('-' * left_dash + '*' + inner_dash * '-' + '*' + '-' * right_dash)
    inner_dash += 1
    right_dash -= 1

mid_range = n // 2
star = left_dash
inner_dash = n - 1
right_dash = n - 1

for row in range(mid_range):
    print('*' * star + '*' + '-' * inner_dash + '*' + '-' * right_dash)

bottom_range = mid_range

for row in range(bottom_range):
    if row == bottom_range - 1:
        print('-' * left_dash + '*' + '*' * inner_dash + '*' + '-' * right_dash)
    else:
        print('-' * left_dash + '*' + '-' * inner_dash + '*' + '-' * right_dash)
    left_dash -= 1
    right_dash -= 1
    inner_dash += 2