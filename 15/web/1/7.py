def f(x, A):
    return (x & 29 == 0) or ((x & 11 == 0) <= (not(x & A == 0)))

print(min(A for A in range(0, 200) if all(f(x, A) == 1 for x in range(10, 200))))
