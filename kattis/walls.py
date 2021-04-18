import math
def distance(x1, y1, x2, y2):
  return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def all_used(x):
  for p in x:
    if not p:
      return False
  return True

l, w, n, r = [int(x) for x in input().split()]

centers = [(-l/2, 0), (l/2, 0), (0, -w/2), (0, w/2)]

reachable_walls = []

for cn in range(n):
   x, y = [int(x) for x in input().split()]
   reachable_walls.append([])
   for i, center in enumerate(centers):
     if distance(center[0], center[1], x, y) <= r:
       reachable_walls[-1].append(i)


reachable_walls.sort(key=lambda x: len(x), reverse=True)


def recursive(walls_used, cranes, used):
  if all_used(walls_used):
    global result
    if used < result:
      result = used
    return
  if used == 4:
    return
  if len(cranes) == 0:
    return

  c = walls_used.copy()
  for p in cranes[0]:
    c[p] = True
  recursive(c, cranes[1:], used+1)

  recursive(walls_used, cranes[1:], used)

walls_used = [False] * 4
result = 5
recursive(walls_used, reachable_walls, 0)

if result < 5:
  print(result)
else:
  print("Impossible")
