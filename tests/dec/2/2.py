from itertools import *
def f(w, x, y, z):
    return ((x <= y) or (z == x)) and (w <= z)

t = (
    (0, 0, 1, 1, 1),
    (0, 0, 1, 0, 0),
    (0, 1, 1, 1, 0)
)

for p in permutations('wxyz', r=4):
    if all(f(**dict(zip(p, l))) == l[-1] for l in t):
        print(*p)