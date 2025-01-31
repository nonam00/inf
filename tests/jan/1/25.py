from fnmatch import fnmatch

def d(n):
    arr = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            arr.add(i)
            arr.add(n // i)
    return arr

for i in range(300, 10**7 + 1):
    if fnmatch(str(i), '3*52?'):
        dels = d(i)
        if len(dels) % 2 != 0:
            dels.remove(i)
            print(i, max(dels))