from collections import defaultdict
from queue import PriorityQueue

n, m = [int(x) for x in input().split()]
while m != 0 and n != 0:
  grap = defaultdict(list)
  for _ in range(m):
    data = input().split()
    x = int(data[0])
    y = int(data[1])
    cost = float(data[2])
    
    grap[x].append((y, cost))
    grap[y].append((x, cost))

  values = [-1 for x in range(n)]
  values[0] = 1.0
  visited = [False for x in range(n)]
  q = PriorityQueue()
  q.put((-1, 0))
  while not q.empty():
    (_,a) = q.get()
    if visited[a]:
      continue
    visited[a] = True

    for (b, cost) in grap[a]:
      if values[a]*cost > values[b]:
        values[b] = values[a]*cost
        q.put((-values[b], b))


  print("{:.4f}".format(values[-1]))
  
  n, m = [int(x) for x in input().split()]