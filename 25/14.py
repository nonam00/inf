from fnmatch import fnmatch
def dels(x):
    arr = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            arr.add(i)
            arr.add(x // i)
    return arr

for i in range(10**7 + 1):
    if fnmatch(str(i), '3*52?'):
        D = dels(i)
        if len(D) % 2 != 0:
            D.remove(i)
            print(i, max(D))
