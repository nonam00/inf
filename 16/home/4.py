from functools import lru_cache

@lru_cache(None)
def f(n):
    if n < 3: return n + 1
    if n >= 3 and n % 2 == 0: return f(n - 2) + n - 2
    if n >= 3 and n % 2 != 0: return f(n + 2) + n + 2

count = 0
for n in range(1, 10000):
    try:
        if 10000 <= abs(f(n)) <= 99999:
            count += 1
    except:
        pass
print(count)