from itertools import product, permutations
def f1(x, y, z):
    return (x == (not y)) or ((not x) or z)
def f2(x, y, z):
    return (x == (not y)) or ((not x) and z)
def f3(x, y, z):
    return (x == (not y)) or ((not x) == z)
def f4(x, y, z):
    return (x == (not y)) or ((not x) <= z)

arr = []
for x1, x2, x3, x4, x5, x6 in product([0,1], repeat=6):
    t = (
        (0, x1, x2, 0),
        (x3, 0, x4, 1),
        (x5, x6, 1, 0)
    )
    if len(t) == len(set(t)):
        for p in permutations("xyz", r=3):
            if all(f1(**dict(zip(p, l))) == l[-1] for l in t):
                arr.append(1)
            if all(f2(**dict(zip(p, l))) == l[-1] for l in t):
                arr.append(2)
            if all(f3(**dict(zip(p, l))) == l[-1] for l in t):
                arr.append(3)
            if all(f4(**dict(zip(p, l))) == l[-1] for l in t):
                arr.append(4)
print(*(set(arr)))
