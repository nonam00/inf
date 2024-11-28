from fnmatch import fnmatch
def dels(x):
    arr = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            if i % 2 == 0:
                arr.add(i)
            tmp = x // i
            if tmp % 2 == 0:
                arr.add(tmp)
    return arr
for i in range(65000, 10 ** 6):
    if fnmatch(str(i), '6*97*5?'):
        if len(dels(i)) >= 4:
            print(i, sum(dels(i)))

