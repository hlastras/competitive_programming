from collections import defaultdict

islands = int(input())
thresholds = [0 for _ in range(islands)]
values = [0 for _ in range(islands)]
dead = set()

graph = defaultdict(list)

input() # discard collapsed island
for i in range(1, islands):
  data = [int(x) for x in input().split()]
  thresholds[i] = data[0]
  for p in range(2, len(data), 2):
    isl_num = data[p] - 1
    isl_prov = data[p+1]
    graph[isl_num].append((i, isl_prov))
    values[i] += isl_prov


queue = graph[0]
dead.add(0)
while len(queue) > 0:
  next_queue = []
  for (a, cost) in queue:
    if a not in dead:
      values[a] -= cost
      if values[a] < thresholds[a]:
        dead.add(a)
        next_queue.extend(graph[a])
  queue = next_queue

print(islands - len(dead))