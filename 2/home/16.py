from itertools import *
def f(a, b, c, d):
    return ((not a) and (not b)) or (b == c) or d
for x1, x2, x3, x4 in product([0, 1], repeat=4):
    t = (
        (x1, x2, 1, x3, 0),
        (1, 0, x4, 1, 0),
        (0, 0, 1, 1, 0)
    )

    if len(t) == len(set(t)):
        for p in permutations('abcd', r=4):
            if all(f(**dict(zip(p, l))) == l[-1] for l in t):
                print(*p)