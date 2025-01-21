from functools import lru_cache
@lru_cache(None)
def f(n):
    if n < 3: return 2 ** 1024
    if n > 2: return 2 * n + 3 + f(n - 2)
for i in range(0, 4048): f(i)
print(f(4048) - f(16))