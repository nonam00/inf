def f1(c, a, d, b):
    return ((a and b) == (not c)) and (b and d)
def f2(c, a, d, b):
    return ((a and b) == (not c)) and (b or d)
def f3(c, a, d, b):
    return ((a and b) == (not c)) and (b <= d)
def f4(c, a, d, b):
    return ((a and b) == (not c)) and (b == d)

t = (
    (1, 0, 0, 0),
    (1, 0, 1, 0),
    (1, 0, 1, 1),
    (1, 1, 0, 0)
)

print(all(f1(*l) for l in t))
print(all(f2(*l) for l in t))
print(all(f3(*l) for l in t))
print(all(f4(*l) for l in t))
