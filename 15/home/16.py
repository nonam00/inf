def f(x, y, A):
    return (x >= 11) or (3 * x < y) or (x * y < A)
print(min(A for A in range(0, 500) if all(f(x,y,A) for x in range(0, 500) for y in range(0, 500))))
