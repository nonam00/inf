def d(n, m):
    return n % m == 0
def f(x, A):
    return (A + x < 123) <= (d(x, 5) <= (not d(x, 7)))

# A и x - НАТУРАЛЬНЫЕ
print(min(A for A in range(1, 200) if all(f(x, A) == 1 for x in range(1, 400))))
