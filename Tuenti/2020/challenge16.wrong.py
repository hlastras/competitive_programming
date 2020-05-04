c = int(input())

for case in range(1, c+1):
  employees = []
  f, g = [int(x) for x in input().split()]
  for _ in range(g):
    e, _ = [int(x) for x in input().split()]
    access = [int(x) for x in input().split()]
    for _ in range(e):
      employees.append(access.copy())

  employees.sort(key=len)

  rooms = []
  for _ in range(f):
    rooms.append([])

  for e in employees:
    # Find room with few employees aded
    index, length = min(map(lambda x: [x, len(rooms[x])], e), key=lambda x: x[1])
    rooms[index].append(e)
  
  result = max(map(len, rooms))

  print("Case #%d: %d" % (case, result))