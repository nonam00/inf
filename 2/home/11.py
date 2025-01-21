from itertools import *

def f(w, x, y, z):
    return (w or x or y) <= ((y or z) and x or y and (w or z))

for x1, x2, x3, x4, x5 in product([0, 1], repeat=5):
    t = (
        (0, 0, 0, x1, 0),
        (x2, 1, 1, x3, 0),
        (x4, 1, x5, 1, 0)
    )

    if len(t) == len(set(t)):
        for p in permutations('wxyz', r=4):
            if all(f(**dict(zip(p, l))) == l[-1] for l in t):
                print(*p)