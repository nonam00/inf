from itertools import *
def f1(w, x, y, z):
    return (w == x) and (y <= z)
def f2(w, x, y, z):
    return (w <= x) <= (y == z)
for x1, x2, x3, x4, x5 in product([0, 1], repeat=5):
    t = (
        (1, x1, 1, 1, 1, 0),
        (x2, 1, 0, 0, 1, x3),
        (x4, 0, 0, x5, 0, 0)
    )

    if len(t) == len(set(t)):
        for p in permutations('wxyz', r=4):
            if all((f1(**dict(zip(p, l))) == l[-2] and f2(**dict(zip(p, l))) == l[-1]) for l in t):
                print(*p)