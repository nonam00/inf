def f(x, y, A):
    return (2 * y + 3 * x != 135) or (y > A) or (x > A)
print(max(A for A in range(0, 500) if all(f(x, y, A) for x in range(0, 500) for y in range(0, 500))))
