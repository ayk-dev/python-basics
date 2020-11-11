budget = float(input())
n = int(input())
m = int(input())
p = int(input())
#  N видеокарти, M процесора и P на брой рам памет

n_price = n * 250
m_price = 0.35 * n_price * m
p_price = 0.1 * n_price * p

total_bill = n_price + m_price +p_price

if n > m:
    total_bill -= 0.15 * total_bill

if budget >= total_bill:
    money_over = budget - total_bill
    print(f'You have {money_over:.2f} leva left!')
else:
    money_short = total_bill - budget
    print(f'Not enough money! You need {money_short:.2f} leva more!')
