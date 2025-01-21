from itertools import *
def f(w, x, y, z):
    return (w and y) or ((x <= w) == (y <= z))

for x1, x2, x3, x4, x5, x6 in product([0, 1], repeat=6):
    t = (
        (x1, x2, x3, 1, 0),
        (1, x4, x5, 1, 0),
        (1, x6, 1, 1, 0)
    )

    if len(t) == len(set(t)):
        for p in permutations('wxyz', r=4):
            if all(f(**dict(zip(p, l))) == l[-1] for l in t):
                print(*p)