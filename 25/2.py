from fnmatch import fnmatch
for i in range(151, 10 ** 9 + 1, 151):
    if fnmatch(str(i), '2?34?56?8'):
        print(i, i // 151)

