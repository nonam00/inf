from fnmatch import fnmatch
def dels(x):
    arr = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            arr.add(i)
            arr.add(x // i)
    return arr

for i in range(1, int((10 ** 9) ** 0.5) + 1):
    if fnmatch(str(i ** 2), '15*3*09'):
        D = dels(i ** 2)
        if len(D) == 9:
            D.remove(i ** 2)
            print(i ** 2, max(D))
