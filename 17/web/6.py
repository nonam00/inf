a = [int(x) for x in open("")]
mn = min(x for x in a if 100 <= abs(x) <= 999 and len(str(x)) == len(set(str(x))))
r = []
for i in range(len(a) // 2):
    if (a[i] * a[-i - 1]) % mn == 0:
        r.append(a[i] + a[-i - 1])

print(len(r), min(r))
