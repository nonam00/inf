def f(x, A):
    return ((x & 500 != 0) and (x & 200 == 0)) <= (not(x & A == 0))
print(min(A for A in range(0, 500) if all(f(x, A) for x in range(0, 500))))
