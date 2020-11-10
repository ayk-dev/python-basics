num = int(input())

counter = 1
is_counter_bigger_than_num = False


for r in range(1, num + 1):
    for c in range(1, r + 1):
        if counter > num:
            is_counter_bigger_than_num = True
            break
        print(counter, end='')
        counter += 1
    print()
    if is_counter_bigger_than_num:
        break

