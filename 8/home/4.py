from itertools import product
count = 0
bad = [str(20 + i) for i in range(0, 6, 2)] + [str(i) + str(2) for i in range(0, 6, 2)]
print(bad)
for item in list(product(range(0, 6), repeat=7)):
    it = ''.join(map(str, item))
    if item[0] != 0 and item.count(2) == 1 and all(i not in it for i in bad):
        count += 1
print(count)