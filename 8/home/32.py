from itertools import *
letters = sorted(list('АПРЕЛЬ'))[::-1]
count = 0
for item in list(product(letters, repeat=5))[0:387]:
    if item[-1] == 'Ь':
        count += 1
print(count)