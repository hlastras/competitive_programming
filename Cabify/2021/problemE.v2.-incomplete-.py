from collections import defaultdict
from queue import PriorityQueue

k, n, m, o = [int(x) for x in input().split()]
graph = defaultdict(list)

for _ in range(m):
  a, b, t = [int(x) for x in input().split()]
  graph[a].append((b, t))

for _ in range(o):
  start, end = [int(x) for x in input().split()]

  values = [-1 for x in range(n)]
  values[start] = 0
  visited = [False for x in range(n)]
  q = PriorityQueue()
  q.put((0, start))
  while not q.empty():
    (_,a) = q.get()
    if visited[a]:
      continue
    visited[a] = True

    for (b, cost) in graph[a]:
      if values[b] == -1 or values[a] + cost < values[b]:
        values[b] = values[a] + cost
        q.put((values[b], b))

  print(values[end])
