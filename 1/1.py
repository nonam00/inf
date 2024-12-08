from itertools import *

s = '347 3456 1245 1237 236 25 14'.split()
v = 'BA BC CA AD CD CE DE FE EG DF FG'.split()
for p in permutations('ABCDEFG'):
    if all(str(p.index(b) + 1) in s[p.index(a)] for a, b in v):
        print(*p)
