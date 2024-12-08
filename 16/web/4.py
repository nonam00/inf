from functools import lru_cache

@lru_cache(None)
def f(n):
    if n >= 3210: return 1
    if n < 3210: return f(n + 3) + 7

@lru_cache(None)
def g(n):
    if n < 10: return n
    if n >= 10: return g(n - 3) + 5

for n in range(3210, 15, -1): f(n)
for n in range(10, 3000): g(n)

print(f(15) - g(3000))
