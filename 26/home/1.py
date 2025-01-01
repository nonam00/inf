f = open('1.txt')
N = int(f.readline())
izm = [0] * (24 * 60)

for i in range(N):
    zashel, vishel = [int(x) for x in f.readline().split()]
    izm[zashel] += 1
    izm[vishel] -= 1

v_magazine = 0
m = -float('inf')
for minuta in range(1440):
    v_magazine += izm[minuta]
    m = max(m, v_magazine)

v_magazine = 0
koli4estvo_pikov = 0
for minute in range(1440):
    v_magazine += izm[minute]
    if v_magazine == m and izm[minute] != 0:
        koli4estvo_pikov += 1

print(m, koli4estvo_pikov)
