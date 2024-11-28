from fnmatch import fnmatch
def f(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))
for i in range(10 ** 7):
    if fnmatch(str(i), '3?1111*') and f(i):
        print(i)
