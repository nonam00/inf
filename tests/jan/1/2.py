from itertools import *

def f(w, x, y, z):
    return (x and (not y)) or (x == z) or w

for x1, x2, x3, x4 in product([0, 1], repeat=4):
    t = (
        (x1, x2, 0, 1, 0),
        (1, 0, x3, 1, 0),
        (1, 1, 0, x4, 0)
    )

    if len(t) == len(set(t)):
        for p in permutations('wxyz', r=4):
            if all(f(**dict(zip(p, l))) == l[-1] for l in t):
                print(*p)