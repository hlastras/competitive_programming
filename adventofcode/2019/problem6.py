import sys
lines = sys.stdin.read().split("\n")
graph = {}
for line in lines:
  a, b = line.split(")")
  if a not in graph:
    graph[a] = []

  graph[a].append(b)

values = {'COM': 0}
nexts = [('COM', graph['COM'])]

while len(nexts) > 0:
  root, orbits = nexts.pop()
  value = values[root]
  for p in orbits:
    values[p] = value+1
    if p in graph:
      nexts.append((p, graph[p]))

count = 0
for x in values.keys():
  count += values[x]
  
print(count)

