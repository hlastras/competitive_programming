import sys

def find(parent, x):
  while x != parent[x]: 
    x = parent[x]
  return x

def union(parent, cf, x, y):
  a = find(parent, x)
  b = find(parent, y)
  if a == b:
    return b
  if cf[b] < cf[a]:
    a, b = b, a
  parent[a] = b
  cf[b] += cf[a]
  return b


lines = sys.stdin.read().split("\n")
lines.reverse()

cases = int(lines.pop())
res = []
for _ in range(cases):
  q = int(lines.pop())
  name_count = 0
  names = {}
  parent = list(range(q*2))
  cf = [1] * (q * 2)
  for _ in range(q):
    a, b = lines.pop().split()
    if a not in names:
      names[a] = name_count
      name_count += 1
    if b not in names:
      names[b] = name_count
      name_count += 1

    
    res.append(str(cf[union(parent, cf, names[a], names[b])]))
  

print("\n".join(res))

    

