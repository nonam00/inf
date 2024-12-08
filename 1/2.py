from itertools import *

gr = '347 3456 1245 1237 236 25 14'.split()
roads = 'BA BC CA AD CD CE DE FE EG DF FG'.split()
for p in permutations('ABCDEFG'):
    d = dict(zip(p, range(1, 8)))
    if all(str(d[y]) in gr[d[x] - 1] for x, y in roads):
        print(*p)
