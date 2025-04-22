from math import dist

f = open('27_A_18882.txt')
data = []
for line in f:
  data.append([float(x) for x in line.split()])

def get_cluster(p0):
  cluster = [p for p in data if dist(p0, p) < 1]
  if len(cluster) != 0 :
    for p in cluster:
      data.remove(p)
    next_clusters = [get_cluster(p) for p in cluster]
    cluster += sum(next_clusters, [])
  return cluster

clusters = []
while len(data) != 0:
  cluster = get_cluster(data[0])
  clusters.append(cluster)

def centroid(cluster):
    m = []
    for p in cluster:
        sm = sum(dist(p, p1) for p1 in cluster)
        m.append([sm, p])
    return min(m)[1]

centroids = [centroid(cluster) for cluster in clusters]
px = sum(x for x, y in centroids) / len(centroids) * 10000
py = sum(y for x, y in centroids) / len(centroids) * 10000
print(px, py)
