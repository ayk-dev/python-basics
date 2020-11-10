# От конзолата се четат точно 3 числа, всяко на отделен ред:
# Броя клиенти мъже - цяло число в интервала [1...100]
# Броя клиенти жени - цяло число в интервала [1...100]
# Максималният брой маси - цяло число в интервала [1...100]

men = int(input())
women = int(input())
max_tables = int(input())

counter = 0
is_done = False

while not is_done:
    for m in range(1, men + 1):
        for w in range(1, women + 1):
            max_tables -= 1
            counter += 1
            if counter > men * women or max_tables < 0:
                is_done = True
                break
            else:
                print(f'({m} <-> {w})', end=' ')

        if is_done:
            break

