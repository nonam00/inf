clustersA = [[], []]
clustersB = [[], [], []]

for line in open('4A.txt'):
    x, y = [float(k) for k in line.replace(',', '.').split()]
    if x > 4:
        clustersA[0].append([x, y])
    else:
        clustersA[1].append([x, y])
for line in open('4B.txt'):
    x, y = [float(k) for k in line.replace(',', '.').split()]
    if y > (-5/8) * x + (61/8):
        clustersB[0].append([x, y])
    elif (y < -6 * x + 9) or (y < -1.2 * x + 5):
        clustersB[1].append([x, y])
    else:
        clustersB[2].append([x, y])

def d(A, B):
    x1, y1 = A
    x2, y2 = B
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def center(cl):
    arr = []
    for s in cl:
        sm = sum(d(s, s1) for s1 in cl)
        arr.append([sm, s])
    return min(arr)[1]

centersA = [center(cl) for cl in clustersA]
centersB = [center(cl) for cl in clustersB]

pxA = sum(x for x, y in centersA) / 2 * 100000
pyA = sum(y for x, y in centersA) / 2 * 100000
pxB = sum(x for x, y in centersB) / 3 * 100000
pyB = sum(y for x, y in centersB) / 3 * 100000

print(int(pxA), int(pyA))
print(int(pxB), int(pyB))