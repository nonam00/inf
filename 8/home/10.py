from itertools import product
count = 0
bad = ['16', '61', '36', '63', '56', '65', '76', '67']
for item in product(range(0, 8), repeat=5):
    it = ''.join(map(str, item))
    if item[0] != 0 and item.count(6) == 1 and all(i not in it for i in bad):
        count += 1
print(count)