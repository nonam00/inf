from itertools import *
def f(w, x, y, z):
    return ((x or y) == (y <= z)) or w
for x1, x2, x3, x4, x5, x6, x7, x8 in product([0, 1], repeat=8):
    t = (
        (x1, 1, x2, x3, 0),
        (x4, x5, x6, 1, 0),
        (1, x7, x8, 1, 0)
    )

    if len(t) == len(set(t)):
        for p in permutations('wxyz', r=4):
            if all(f(**dict(zip(p, l))) == l[-1] for l in t):
                print(*p)