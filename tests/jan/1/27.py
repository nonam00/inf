clustersA = [[], [], []]
clustersB = [[], [], [], []]

for line in open('27A.txt'):
    x, y = map(float, line.replace(',', '.').split())
    if x < 8:
        clustersA[0].append([x, y])
    elif y < 23:
        clustersA[1].append([x, y])
    else:
        clustersA[2].append([x, y])

for line in open('27B.txt'):
    x, y = map(float, line.replace(',', '.').split())
    if y > 15:
        if x < 13:
            clustersB[0].append([x, y])
        else:
            clustersB[1].append([x, y])
    else:
        if x < 15.5:
            clustersB[2].append([x, y])
        else:
            clustersB[3].append([x, y])

def d(A, B):
    x1, y1 = A
    x2, y2 = B
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def centers(cl):
    arr = []
    for s in cl:
        sm = sum(d(s, s1) for s1 in cl)
        arr.append([sm, s])
    return min(arr)[1]

centersA = [centers(a) for a in clustersA]
centersB = [centers(a) for a in clustersB]

pxA = sum(x for x, y in centersA) / 3 * 10000
pyA = sum(y for x, y in centersA) / 3 * 10000
pxB = sum(x for x, y in centersB) / 4 * 10000
pyB = sum(y for x, y in centersB) / 4 * 10000

print(int(pxA), int(pyA))
print(int(pxB), int(pyB))