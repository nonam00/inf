def f(A, x):
    return ((x & 52 != 0) and (x & 36 == 0)) <= (not (x & A == 0))

print(min(A for A in range(0, 200) if all(f(A, x) for x in range(0, 200))))