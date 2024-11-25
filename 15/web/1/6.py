def f(x, A):
    return ((x & 103 == 0) and (x & 94 != 0)) <= (x & A != 0)

print(min(A for A in range(0, 200) if all(f(x, A) == 1 for x in range(1, 400))))
