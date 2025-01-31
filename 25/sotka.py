def dels(x):
    arr = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            arr.add(i)
            arr.add(x // i)
    return arr

for i in range(int(123456789 ** 0.5), int(223456789 ** 0.5) + 1):
    D = dels(i ** 2)
    if len(D) == 3:
        print(i ** 2, max(D))
