from fnmatch import fnmatch

def dels(n):
    arr = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            arr.add(i)
            arr.add(n // i)
    arr.remove(n)
    return arr

for i in range(15000, 160_000_000):
    if fnmatch(str(i), '15*3*09'):
        d = dels(i)
        if len(d) == 8:
            print(i, max(d))