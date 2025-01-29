def f(x, A):
    return (x & 49 == 0) <= ((x & 28 != 0) <= (x & A != 0))
print(min(A for A in range(0, 500) if all(f(x, A) for x in range(0, 500))))
