def PLOS(a, b, c):
    return a * b > c
def f(x, y, A):
    return not PLOS(x, y, A+13) <= PLOS(28, 6, 520) or PLOS(x, 25, 800)

print(max(A for A in range(-13, 500) if all(f(x, y, A) == 1 for x in range(1, 1000) for y in range(1, 1000))))
