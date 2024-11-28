from fnmatch import fnmatch
count = 0
arr = []
for i in range(4546, 10**10 + 1, 4546):
    if fnmatch(str(i), '8*80*06'):
        if count % 60 == 0:
            print(i, i // 4546)
        count += 1
