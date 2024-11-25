def f(x, y, A):
    return (x + 2 * y < A) or (y > x) or (x > 60)

print(min(A for A in range(0, 200) if all(f(x, y, A) == 1 for x in range(0, 400) for y in range(0, 400))))

