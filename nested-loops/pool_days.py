import math
number_of_people = int(input())
entrance_fee = float(input())
price_chair = float(input())
price_umbrella = float(input())

total_entrance_fee = number_of_people * entrance_fee
total_umbrellas = math.ceil(number_of_people / 2)
total_chairs = math.ceil(0.75 * number_of_people)

chairs_cost = total_chairs * price_chair
umbrellas_cost = total_umbrellas * price_umbrella

total_expenses = total_entrance_fee + chairs_cost + umbrellas_cost

print(f'{total_expenses:.2f} lv.')



