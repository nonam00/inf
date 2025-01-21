from itertools import *
letters = sorted(list('ABCX'))
count = 0
for item in product(letters, repeat=5):
    if (item[-1] == 'X' and item.count('X') == 1) or item.count('X') == 0:
        count += 1
print(count)