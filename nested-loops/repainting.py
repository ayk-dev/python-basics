# заплаща на майсторите за 1 час работа, е равна на 30% от сбора на всички разходи за материали.

naylon_required = int(input())
paint_required = int(input())
thinner = int(input())
hours_working = int(input())

total_paint = paint_required + 0.1 * paint_required
total_naylon = naylon_required + 2

naylon_cost = total_naylon * 1.50
paint_cost = total_paint * 14.50
thinner_cost = thinner * 5
materials = naylon_cost + paint_cost + thinner_cost + 0.40 # 0.40 for bags
workers_cost = 0.30 * materials * hours_working

total_expenses = materials + workers_cost

print(f'Total expenses: {total_expenses:.2f} lv.')


