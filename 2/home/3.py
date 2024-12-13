from itertools import permutations, product
def f(x, y, z):
    return (not z) and x or x and y
t = (
    (0, 0, 0, 0),
    (0, 0, 1, 1),
    (0, 1, 0, 0),
    (0, 1, 1, 1),
    (1, 0, 0, 0),
    (1, 0, 1, 0),
    (1, 1, 0, 0),
    (1, 1, 1, 1)
)
for p in permutations('xyz'):
    if (all([f(**dict(zip(p,l))) == l[-1] for l in t])):
        print(*p)
