from itertools import *
def f(w, x, y, z):
    return ((x and (not y)) <= (z and w)) and ((y <= z) or (w <= x))

for x1, x2, x3, x4, x5, x6 in product([0, 1], repeat=6):
    t = (
        (x1, x2, 1, 1, 0),
        (1, x3, 1, x4, 0),
        (x5, 0, x6, 1, 0)
    )

    if len(t) == len(set(t)):
        for p in permutations('wxyz', r=4):
            if all(f(**dict(zip(p, l))) == l[-1] for l in t):
                print(*p)