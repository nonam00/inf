def f(n):
    if n <= 1: return n
    if n > 1 and n % 3 == 0: return f(n - 1) + f(n - 2) + 1
    if n > 1 and n % 3 != 0: return g(n - 3)

def g(n):
    if n > 100: return n
    if n <= 100: return g(n + 2) + 1

for i in range(100, 0, -1): g(i)

print(f(15) + f(12))