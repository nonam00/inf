from functools import lru_cache

@lru_cache(None)
def f(n):
    if n < 3: return 2
    if n > 2: return 2 * f(n - 2)

for i in range(2, 2223): f(i)

print(f(2222) / f(2182))
