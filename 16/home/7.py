from functools import lru_cache

@lru_cache(None)
def f(n):
    if n <= 1: return n
    if n > 1 and n % 3 == 0: return n + f(n / 3)
    if n > 1 and n % 3 != 0: return n + f(n + 3)

for n in range(0, 10009):
    try:
        if f(n) > 100:
            print(n)
    except:
        pass  
