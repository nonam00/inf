from itertools import *
def f(u, w, x, y, z):
    return ((z <= w) and (y == (not x))) <= (u == (y or z))
for x1, x2, x3, x4, x5, x6, x7, x8 in product([0, 1], repeat=8):
    t = (
        (0, x1, 0, 0, 0, 0),
        (0, x2, x3, 0, 0, 0),
        (x4, 0, 0, 0, x5, 0),
        (0, 0, x6, x7, x8, 0)
    )

    if len(t) == len(set(t)):
        for p in permutations('uwxyz', r=5):
            if all(f(**dict(zip(p, l))) == l[-1] for l in t):
                print(*p)