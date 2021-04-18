from collections import defaultdict
from sys import stdin
lines = stdin.read().split("\n")
lines.reverse()

islands = int(lines.pop())
t = [0 for _ in range(islands)]
v = [0 for _ in range(islands)]
graph = defaultdict(list)

lines.pop() # discard collapsed island
for i in range(1, islands):
  data = [int(x) for x in lines.pop().split()]
  t[i] = data[0]
  for p in range(2, len(data), 2):
    isl_num = data[p] - 1
    isl_prov = data[p+1]
    graph[isl_num].append((i, isl_prov))
    v[i] += isl_prov

dead = set()
dead.add(0)
q = graph[0]
while len(q) > 0:
  nex = []
  for (a, cost) in q:
    if a not in dead:
      v[a] -= cost
      if v[a] < t[a]:
        dead.add(a)
        nex.extend(graph[a])
  q = nex

print(islands - len(dead))