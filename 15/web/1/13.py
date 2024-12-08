def f(x, y, A):
    return (x - y >= 39) or (y <= x) or (y >= A - 20)
print(max(A for A in range(0, 400) if all(f(x, y, A) == 1 for x in range(1, 1000) for y in range(1, 1000))))
