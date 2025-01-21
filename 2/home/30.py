from itertools import *
def f(x, y, z):
    return not(x == (y <= z))

t = (
    (0, 0, 1, 1),
    (0, 1, 1, 0)
)

for p in permutations('xyz', r=3):
    if all(f(**dict(zip(p, l))) == l[-1] for l in t):
        print(*p)