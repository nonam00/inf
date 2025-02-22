def p(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))

def dels(x):
    arr1 = set()
    arr2 = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            tmp = x // i
            if i % 2 == 0:
                arr1.add(i)
            if p(i):
                arr2.add(i)
            if tmp % 2 == 0:
                arr1.add(tmp)
            if p(tmp):
                arr2.add(tmp)
    return [arr1, arr2]

for i in range(10 ** 8 + 1, 10 ** 8 + 1000):
    D = dels(i)
    arr1, arr2 = D[0], D[1]
    if len(arr1) == len(arr2):
        print(i, abs(sum(arr2) - sum(arr1)))

