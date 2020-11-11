n1 = int(input()) # цяло число в интервала [1...999]
n2 = int(input()) # Втори ред – край на интервала – цяло число в интервала [по-голямо от първото число...1000]
m = int(input()) # Трети ред – магическото число – цяло число в интервала [1...10000]
counter = 0
flag = False
for x in range(n1, n2 + 1):
    for y in range(n1, n2 + 1):
        counter += 1
        sum = x + y
        if sum == m:
            flag = True
            break
    if flag:
        print(f'Combination N:{counter} ({x} + {y} = {m})')
        break

if not flag:
    print(f'{counter} combinations - neither equals {m}')




