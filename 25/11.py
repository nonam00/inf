from fnmatch import fnmatch
for i in range(28, 10**9 + 1, 28):
    if fnmatch(str(i), '6323*353?'):
        print(i, i // 28)
