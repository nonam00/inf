def f(x, y, A):
    return (x + y <= 32) or (y <= x + 4) or (y >= A)
print(max(A for A in range(0, 1000) if all(f(x, y, A) for x in range(0, 1000) for y in range(0, 1000))))
