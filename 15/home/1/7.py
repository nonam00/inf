def DEL(n, m):
    return n % m == 0
def f(x, A):
    return (DEL(x, 3) <= (not(DEL(x, 2)))) or (x - A >= 4)
print(max(A for A in range(1, 500) if all(f(x,A) for x in range(1,500))))
