from itertools import *
def f(a, b, c):
    return a and (not b) or c
t = (
    (0, 0, 0, 0),
    (0, 0, 1, 1),
    (0, 1, 0, 1),
    (0, 1, 1, 1),
    (1, 0, 0, 0),
    (1, 0, 1, 0),
    (1, 1, 0, 1),
    (1, 1, 1, 1)
)

for p in permutations('abc', r=3):
    if all(f(**dict(zip(p, l))) == l[-1] for l in t):
        print(*p)