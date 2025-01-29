def f(x, y, A):
    return (x + 2 * y < A) or (y > x) or (x > 60)
print(min(A for A in range(0, 200) if all(f(x,y,A) for x in range(0, 200) for y in range(0, 200))))
