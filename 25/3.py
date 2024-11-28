from fnmatch import fnmatch 
def deliteli(x):
    dels = set() 
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            dels.add(i)
            dels.add(x // i)
    return dels
for x in range(500000, 505000):
    dels = sum(deliteli(x))
    if fnmatch(str(dels), '*7?'):
        print(x, dels)

    
