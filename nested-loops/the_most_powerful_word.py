import math
word = input()

sum = 0 # sum of letters in a word
max_sum = 0
mpw = '' # most powerful word

while word != 'End of words':
    sum = 0
    for l in range(len(word)):
        value = ord(word[l]) # value of letter
        sum += value
    if word[0] == 'A' or word[0] == 'E' or word[0] == 'I' or word[0] == 'O' or word[0] == 'U' or word[0] == 'Y' or word[0] == 'a' or word[0] == 'e' or word[0] == 'i' or word[0] == 'o' or word[0] == 'u' or word[0] == 'y':
        sum *= len(word)
    else:
        sum /= len(word)
    if sum > max_sum:
        max_sum = sum
        mpw = word
    word = input()

print(f'The most powerful word is {mpw} - {math.floor(max_sum)}')