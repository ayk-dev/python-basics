n = int(input())

star = 1
outer_underscore = 0
inner_underscore = 0
end_range = 0

if n % 2 == 0:
    end_range = n-1
else:
    end_range = n

for row in range(0, end_range):
    if n % 2 == 0:
        if row <= end_range / 2:
            inner_underscore = 2 * row
            outer_underscore = (n - 1) // 2 - row

            print(outer_underscore * '_' + '*' + inner_underscore * '_' + '*' + outer_underscore * '_')
    else:
        outer_underscore = (n // 2) - row
        inner_underscore = n - (2 * outer_underscore + 2* star)
        if 1 <= row < (n+1)/2:
            print('_' * outer_underscore + '*' + inner_underscore * '_' + '*' + '_' * outer_underscore)
        else:
            print('_' * outer_underscore + '*' + '_' * outer_underscore)







