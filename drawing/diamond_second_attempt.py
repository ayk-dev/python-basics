n = int(input())

is_n_even = n % 2 == 0
end_range = ''
outer_score = ''
inner_score = ''

if is_n_even:
    end_range = n - 1
    outer_score = (n / 2) - 1
    inner_score = n - (2 * outer_score + 2)
else:
    end_range = n
    outer_score = n // 2
    inner_score = n - (1 + 2 * outer_score)

for row in range(0, end_range):
    if row == 0 or row == end_range - 1:
        if is_n_even:
            print('_' * outer_score + '**' + outer_score)



