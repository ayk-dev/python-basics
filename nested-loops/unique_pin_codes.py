import math
a = int(input()) # Горната граница на първото число - цяло число в диапазона [1...9]
b = int(input()) # Горната граница на второто число - цяло число в диапазона [1...9]
c = int(input()) # Горната граница на третото число - цяло число в диапазона [1...9]

unique_pin = ''

# Първата и третата цифра трябва да бъдат четни.
# Втората цифра трябва да бъде просто число в диапазона [2...7].

for x in range(1, a + 1):
    for y in range(1, b + 1):
        end_i = int(math.sqrt(y))
        for i in range(2, end_i + 1):
            for z in range(1, c + 1):
                if x % 2 == 0 and z % 2 == 0 and y / i == y // i:
                    unique_pin = f'{x} {y} {z}'
                    print(unique_pin)




