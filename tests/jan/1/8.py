from itertools import product

letters = sorted(list('КОМПЬЮТЕР'))
ix = -1
for i, item in enumerate(product(letters, repeat=5)):
    if (i + 1) % 2 != 0 and item[0] != 'Ь' and item.count('К') == 2:
       ix = i + 1
print(ix) 