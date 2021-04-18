def find(parent, x):
  while x != parent[x]: 
    x = parent[x]
  return x

def union(parent, x, y):
  parent[find(parent, x)] = find(parent, y)

cases = int(input())

for _ in range(cases):
  stores = int(input())
  uf = list(range(stores+2))

  points = []
  for _ in range(stores+2):

    x, y = [int(x) for x in input().split()]
    for i, (x2, y2) in enumerate(points):
      distance = abs(x2 - x) + abs(y2 - y)
      if distance <= 1000:
        union(uf, i, len(points))

    points.append((x, y))


  if find(uf, 0) == find(uf, len(points)-1):
    print("happy")
  else:
    print("sad")
