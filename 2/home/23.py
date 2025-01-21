from itertools import *
def f(w, x, y, z):
    return ((w <= y) and ((not x) <= z)) <= ((z == w) or (y and (not x)))

for x1, x2, x3, x4, x5 in product([0, 1], repeat=5):
    t = (
        (1, 1, x1, 1, 0),
        (0, 0, 0, x2, 0),
        (0, x3, x4, x5, 0)
    )

    if len(t) == len(set(t)):
        for p in permutations('wxyz', r=4):
            if all(f(**dict(zip(p, l))) == l[-1] for l in t):
                print(*p)