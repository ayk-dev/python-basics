n = int(input())

is_special = False
divider = 0

for num in range(1111, 10000):
    number = str(num)
    for i in range(0, 4):
        divider = int(number[i])
        if divider != 0 and divider <= n and n % divider == 0:
            is_special = True
        else:

            is_special = False
            break
    if is_special:
        print(num, end=' ')




