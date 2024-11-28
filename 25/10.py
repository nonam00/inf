from fnmatch import fnmatch

def dels(x):
    arr = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            if fnmatch(str(i), '4*'):
                arr.add(i)
            if fnmatch(str(x // i), '4*'):
                arr.add(x // i)
    return arr

for x in range(1, 10**6):
    arr = dels(x)
    if len(arr) == 24:
        print(x, max(arr))

