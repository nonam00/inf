from itertools import permutations, product

def f(x, y, w, z):
    return (not (x <= z)) or (y == w) or y

for x1, x2, x3, x4, x5, x6, x7 in product([0, 1], repeat=7):
    t = (
        (1, 0, x1, x2, 0),
        (x3, 1, 0, x4, 0),
        (0, x5, x6, x7, 0)
    )
    if len(t) == len(set(t)):
        for p in permutations('xywz', r=4):
            if all(f(**dict(zip(p, l))) == l[-1] for l in t):
                print(*p)

