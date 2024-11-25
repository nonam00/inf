def DEL(n, m):
    return n % m == 0
def f(x, A):
    return(DEL(x, 13) <= (not(x in range(40, 61)))) or (A < x + 20)
print(max(A for A in range(1, 400) if all(f(x,A) for x in range(1, 400))))
