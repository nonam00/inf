def f(x, y, A):
    return (x * y < A) or (x < y) or (9 < x)
print(min(A for A in range(0, 200) if all(f(x, y, A) for x in range(0, 200) for y in range(0, 200))))
