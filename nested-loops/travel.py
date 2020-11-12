destination = input()

while destination != 'End':
    min_budget = float(input())
    total_saved = 0
    while total_saved < min_budget:
        money_saved = float(input())
        total_saved += money_saved

    print(f'Going to {destination}!')
    destination = input()


