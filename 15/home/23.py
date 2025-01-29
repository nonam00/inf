def f(A, x, y):
    return (x * y < A) or (x < y) or (9 < x)

print(min(A for A in range(0, 200) if all(f(A, x, y) for x in range(0, 200) for y in range(0, 200))))