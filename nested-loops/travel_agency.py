town = input() # "Bansko",  "Borovets", "Varna" или "Burgas"
packet = input() # "noEquipment",  "withEquipment", "noBreakfast" или "withBreakfast"
vip_discount = input() # "yes" или "no"
nights = int(input())

price_per_night = 0

if nights < 1:
    print(f'Days must be positive number!')
else:
    if town == 'Bansko' or town == 'Borovets':
        if packet == 'noEquipment':
            price_per_night = 80
            if vip_discount == 'yes':
                price_per_night -= price_per_night * 0.05
        elif packet == 'withEquipment':
            price_per_night = 100
            if vip_discount == 'yes':
                price_per_night -= price_per_night * 0.1
        else:
            print(f'Invalid input!')
    elif town == "Varna" or town == "Burgas":
        if packet == 'noBreakfast':
            price_per_night = 100
            if vip_discount == 'yes':
                price_per_night -= price_per_night * 0.07
        elif packet == 'withBreakfast':
            price_per_night = 130
            if vip_discount == 'yes':
                price_per_night -= price_per_night * 0.12
        else:
            print(f'Invalid input!')
    else:
        print(f'Invalid input!')


if price_per_night > 0:
    total_price = price_per_night * nights
    if nights > 7:
        total_price = price_per_night * (nights - 1)
    print(f'The price is {total_price:.2f}lv! Have a nice time!')

