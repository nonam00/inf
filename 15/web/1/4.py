def _del(x, d):
    return x % d == 0

def f(x, A):
    return (_del(x, 10) and _del(x, 26) and (x >= 300)) <= (A <= x)

print(max(A for A in range(-1000, 1000) if all(f(x, A) == 1 for x in range(1, 2000))))
