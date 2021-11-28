from collections import defaultdict
from queue import PriorityQueue
from math import sqrt
import random
INT_MAX = 9999999999999

def distance(x1, y1, x2, y2, diff_h):
  d = sqrt((x2-x1)**2 + (y2-y1)**2)
  return sqrt(d**2 + diff_h**2)

def solve (i, r, used, current, sol):
  if current > sol[0]:
    return
  if len(used) == len(r):
    sol[0] = current
    return

  for index, value in enumerate(r[i]):
    if index not in used:
      used.add(index)
      solve(i+1, r, used, current+value, sol)
      used.remove(index)

n, s, t, q = [int(x) for x in input().split()]

hills = []
for _ in range(n):
  x, y, h = [int(x) for x in input().split()]
  hills.append((x, y, h))

springs = [int(x)-1 for x in input().split()]
towns = [int(x)-1 for x in input().split()]


### BUILD GRAPH
graph = defaultdict(list)
for i in range(len(hills)):
  for j in range(i+1, len(hills)):
    h1 = hills[i]
    h2 = hills[j]
    if h1[2] != h2[2]: # Different heights
      dist = distance(h1[0], h1[1], h2[0], h2[1], h1[2]-h2[2])
      if dist <= q: # Less than max length
        if h1[2] < h2[2]:
          graph[i].append((j, dist))
        else:
          graph[j].append((i, dist))



### DIKSTRA IN POINT
bests = []
for i in towns:
  values = [-1 for x in range(n)]
  values[i] = 0
  visited = [False for x in range(n)]
  q = PriorityQueue()
  q.put((0, i))
  while not q.empty():
    (_,a) = q.get()
    if visited[a]:
      continue
    visited[a] = True

    for (b, d) in graph[a]:
      curr = values[a] + d
      if values[b] == -1 or curr < values[b]:
        values[b] = curr
        q.put((values[b], b))
      
  
  r = []
  for j in springs:
    if values[j] == -1:
      r.append(INT_MAX)
    else:
      r.append(values[j])
  bests.append(r)


matrix = []
for i in range(20):
  row = []
  for j in range(20):
    row.append(random.randint(1, 1000000))
  matrix.append(row)

bests = matrix

### SOLVE
sol = [INT_MAX]
solve(0, bests, set(), 0, sol)
if sol[0] == INT_MAX:
  print("IMPOSSIBLE")
else:
  print(sol[0])
