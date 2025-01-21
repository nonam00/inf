from itertools import *
def f(a, b, c, t):
    return ((not a) or (not b)) and (c <= (not a)) and (t and (not a) or c and (not b))

t = (
    (1, 0, 0, 1, 0),
    (1, 1, 0, 1, 1),
    (0, 0, 0, 1, 0),
    (1, 0, 0, 0, 1)
)

for p in permutations('abct', r=4):
    if all(f(**dict(zip(p, l))) == l[-1] for l in t):
        print(*p)