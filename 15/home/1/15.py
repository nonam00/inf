def DEL(n, m):
    return n % m == 0
def f(x, A):
    return (DEL(x, 2) <= (not(DEL(x, 3)))) or (x + A >= 100) 
print(min(A for A in range(1, 200) if all(f(x, A) for x in range(1, 200))))
