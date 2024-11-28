from fnmatch import fnmatch
for i in range(2023, 10 ** 9 + 1, 2023):
    if fnmatch(str(i), '20*23'):
        ch = sum(map(int, str(i)))
        if ch % 7 == 0 and ch < 20:
            print(i)

