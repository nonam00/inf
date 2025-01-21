from itertools import *
def f(a, b, c, d):
    return a and (not b) or (a or b) and c or d

for x1, x2, x3, x4, x5, x6, x7, x8 in product([0, 1], repeat=8):
    t = (
        (x1, x2, x3, 1, 0),
        (x4, 1, x5, 1, 0),
        (1, x6, x7, x8, 0)
    )

    if len(t) == len(set(t)):
        for p in permutations('abcd', r=4):
            if all(f(**dict(zip(p, l))) == l[-1] for l in t):
                print(*p)