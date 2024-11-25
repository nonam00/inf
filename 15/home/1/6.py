def f(x, A):
    return ((x & 52 != 0) and (x & 36 == 0)) <= (not(x & A == 0))
print(min(A for A in range(0, 1000) if all(f(x, A) == 1 for x in range(0, 1000))))
