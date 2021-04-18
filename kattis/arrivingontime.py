from collections import defaultdict
from queue import PriorityQueue
n, m, s = [int(x) for x in input().split()]

graph = defaultdict(list)
for _ in range(m):
  u, v, t0, p, d = [int(x) for x in input().split()]
  graph[v].append((u, (t0, p, d)))


def calc(x, d, t0, p):
  if x-d-t0 < 0:
    return -1
  r = ((x-d-t0)//p)*p+t0
  return r

values = [-1 for x in range(n)]
values[-1] = s
visited = [False for x in range(n)]
q = PriorityQueue()
q.put((0, n-1))
while not q.empty():
  (_,a) = q.get()
  if visited[a]:
    continue
  visited[a] = True

  for (b, (t0, p, d)) in graph[a]:
    curr = calc(values[a], d, t0, p)
    if values[b] == -1 or curr > values[b]:
      values[b] = curr
      q.put((-values[b], b))

if values[0] == -1:
  print("impossible")
else:
  print(values[0])