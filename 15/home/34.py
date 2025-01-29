def t(n, m, k):
    return n + m > k and n + k > m and k + m > n
def f(x, A):
    return t(A, 5, x) <= ((max(x, 11) <= 19) == (not t(23, 13, x)))
print(max(A for A in range(1, 500) if all(f(x, A) for x in range(1, 500))))

