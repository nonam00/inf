from functools import lru_cache

@lru_cache(None)
def f(n):
    if n >= 2022: return n
    if n < 2022: return f(n + 5) + 7

for n in range(2222, 49, -1): f(n)

print(f(45) - f(49))
