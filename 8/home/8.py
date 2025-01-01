from itertools import product
count = 0
for item in product('ГЕПАРД', repeat=5):
    if item.count('Г') == 1 and item[0] != 'А' and item[-1] != 'Е':
        count += 1
print(count)