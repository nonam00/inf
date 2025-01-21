from itertools import *

def f(a, b, c):
    return (a == (b or c)) == b 

for x1, x2, x3, x4 in product([0, 1], repeat=4):
    t = (
        (x1, 0, 0, 1),
        (0, x2, x3, 1),
        (0, x4, 0, 1)
    )

    if len(t) == len(set(t)):
        for p in permutations('abc', r=3):
            if all(f(**dict(zip(p, l))) == l[-1] for l in t):
                print(*p)