# exam exercise from Mar. 6, 2016

n = int(input())
slash = 1
backslash = 1
triangle_char = n // 2
underscore = (2 * n) - (2 * slash + 2 * backslash + 2 * triangle_char)

print(slash * '/' + triangle_char * '^' + backslash * "\\" + underscore * '_' + slash * '/' + triangle_char * '^' + backslash * "\\")

for row in range(2, n):
    if row == n - 1:
        print('|' + (triangle_char + slash) * ' ' + '_' * underscore + (triangle_char + slash) * ' ' + '|')
    else:
        print('|' + (2 * n - 2) * ' ' + '|')

print(backslash * '\\' + triangle_char * '_' + slash * '/' + underscore * ' ' + backslash * '\\' + triangle_char * '_' + slash * '/')