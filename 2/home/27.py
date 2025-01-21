from itertools import *
def f(a, b, c, d):
    return d and ((a or (not c)) <= (a and b and (not c)))

for x1, x2, x3, x4 in product([0, 1], repeat=4):
    t = (
        (1, 1, x1, 1, 1),
        (1, x2, 1, 1, 1),
        (1, x3, 1, x4, 1)
    )

    if len(t) == len(set(t)):
        for p in permutations('abcd', r=4):
            if all(f(**dict(zip(p, l))) == l[-1] for l in t):
                print(*p)