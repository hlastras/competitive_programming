from collections import defaultdict
import sys

def calculate(i):
  if i in cache and cache[i] != None:
    return
  
  stack = [i]
  co = 0
  while len(stack) > 0:
    co += 1
    if co%100 == 0:
      tot = sys.getsizeof(cache)
      for _, v in cache.items():
        tot += sys.getsizeof(v)
      print(tot/1024)
      print(len(stack))
    index = stack.pop()
    if len(graph[index]) > 0:
      all_processed = True
      exp = []
      r = {}
      r[index] = 0
      for b, t in graph[index]:
        if b not in cache:
          exp.append(b)
          all_processed = False
        else:
          for key, value in cache[b].items():
            if key not in r:
              r[key] = value + t
            else:
              r[key] = min(value + t, r[key])

      if all_processed:
        cache[index] = r
      else:
        stack.append(index)
        stack.extend(exp)
    else:
      # procesamos hoja
      r = {}
      r[index] = 0
      cache[index] = r
      


k, n, m, o = [int(x) for x in input().split()]
graph = defaultdict(list)
parent = [i for i in range(n)]

for _ in range(m):
  a, b, t = [int(x) for x in input().split()]
  graph[a].append((b, t))



cache = {}
for i in range(o):
  start, end = [int(x) for x in input().split()]

  calculate(start)
  if start in cache and end in cache[start]:
    print(cache[start][end])
  else:
    print(-1)
