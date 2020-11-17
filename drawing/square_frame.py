n = int(input())


def draw_a_row_of_plus_and_minus(num):
    print('+ ' + '- ' * (num-2) + '+')


def draw_middle_rows(num):
    for row in range(0, num - 2):
        print('| ' + '- ' * (num - 2) + '|')


def draw_square_of_signs(num):
    draw_a_row_of_plus_and_minus(num)
    draw_middle_rows(num)
    draw_a_row_of_plus_and_minus(num)


draw_square_of_signs(n)