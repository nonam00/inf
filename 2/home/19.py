from itertools import *
def f(w, x, y, z):
    return ((y and (x == (not z))) <= w) and (z <= y)

for x1, x2, x3, x4, x5 in product([0, 1], repeat=5):
    t = (
        (0, 0, x1, x2, 0),
        (0, x3, 0, 0, 0),
        (1, x4, x5, 1, 0)
    )

    if len(t) == len(set(t)):
        for p in permutations('wxyz', r=4):
            if all(f(**dict(zip(p, l))) == l[-1] for l in t):
                print(*p)