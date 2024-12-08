from functools import lru_cache

@lru_cache(None)
def f(n):
    if n == 1: return 1
    if n > 1: return (n - 1) * f(n - 1)

for n in range(1, 2024): f(n)

print((f(2024) + 2 * f(2023)) / f(2022))
