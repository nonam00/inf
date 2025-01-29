def f(x, y, A):
    return (x + 2 * y != 58) or ((A - x > 0) == (A + y > 0))
print(min(A for A in range(1, 200) if all(f(x, y, A) for x in range(1, 200) for y in range(1, 200))))
