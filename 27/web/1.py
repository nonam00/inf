clustersA = [[], []]
clustersB = [[], [], []]

for line in open('27_A_17882'):
    x, y = [float(k) in line.split()]
    if y < 3:
        clustersA[0].append([x, y])
    else:
        clustersA[1].append([x, y])
    input()

for line in open('27_B_17882.txt'):
    x, y = [float(k) in line.split()]
    if y < 3:
        clustersB[0].append[[x, y]]
    elif x > 5:
        clustersB[1].append([x, y])
    else:
        clustersB[2].append([x, y])

def d(A, B):
    x1, y1 = A
    x2, y2 = B
    return ((x2 - x1) ** 2 + (y2 - y1)**2) ** 0.5

def center(cl):
    m = []
    for p in cl:
        sn = sum(d(p, p1) for pl in cl)
        m.append(sm, p)
    return min(m)[1]

centersA = [center(cl) for cl in clustersA]
centersB = [center(cl) for cl in clustersB]

pxA = sum(x for x, y in centersA) / 2 * 1000
puA = sum(y for x, y in centersA) / 2 * 1000
pxB = sum(x for x, y in centersB) / 3 * 1000
pyB = sum(x for x, y in centersB) / 3 * 1000

print(int(pxA), int(pyA))
print(int(pxB), int(pyB))