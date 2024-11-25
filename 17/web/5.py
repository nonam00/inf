def p(x):
    return x > 1 and all(x % d != 0 for d in range(2, int(x ** 0.5) + 1))
a = [int(x) for x in open("5.txt")]
mx = max(x for x in a if abs(x) % 100 == 17)
r = []
for i in range(len(a) - 2):
    u1 = str(a[i]).count('3') > 0
    u2 = str(a[i + 1]).count('3') > 0
    u3 = str(a[i + 2]).count('3') > 0
    if u1 and u2 and u3:
        if a[i] + a[i + 1] + a[i + 2]:
            if ((a[i] + a[i + 1])) % mx == 0:
                r.append(a[i] * a[i+1])
print(len(r), max(r))

