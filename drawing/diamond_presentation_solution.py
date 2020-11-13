import math
n = int(input())

left_right = (n - 1) // 2 # tereta otlqwo i otdqsno

end_range = math.ceil(n / 2)

for row in range(end_range):
    print('-' * left_right + '*', end='')
    mid = n - 2 * left_right - 2
    if mid >= 0:
        print('-' * mid + '*', end='')
    print('-' * left_right)
    left_right -= 1

# second part solution is mine
left_right = 1
second_part_range = (n - 1) // 2

for row in range(second_part_range):
    mid = n - (2 * left_right + 2)
    print('-' * left_right + '*', end='')
    if mid >= 0:
        print('-' * mid + '*', end='')
    print('-' * left_right)
    left_right += 1


