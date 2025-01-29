def p(a, b, c): return a * b > c
def f(x, y, A):
    return (not p(x, y, A + 13)) <= p(28, y, 520) or p(x, 25, 800)
print(max(A for A in range(-200, 200) if all(f(x, y, A) for x in range(1, 500) for y in range(1, 500))))
