def find_neighbors(i, R, C):
  row = i // C
  col = i % C

  n = []
  if (row - 1) >= 0:
    n.append(i - C)
  else:
    n.append(-1)

  if (col - 1) >= 0:
    n.append(i - 1)
  else:
    n.append(-1)

  if (col + 1) < C:
    n.append(i + 1)
  else:
    n.append(-1)

  if (row + 1) < R:
    n.append(i + C)
  else:
    n.append(-1)

  return n

def average(n, skills):
  s = 0
  t = 0
  for x in n:
    if x != -1:
      s += skills[x]
      t += 1

  if t == 0:
    return 0.0
  else:
    return s / t

def should_remove(i, skills, neighbors):
  n = neighbors[i]
  m = average(n, skills)
  return skills[i] < m

def change_neighbors(i, neighbors, n_check):
  n = neighbors[i]

  if n[0] != -1:
    neighbors[n[0]][3] = n[3]
    n_check.add(n[0])

  if n[1] != -1:
    neighbors[n[1]][2] = n[2]
    n_check.add(n[1])

  if n[2] != -1:
    neighbors[n[2]][1] = n[1]
    n_check.add(n[2])

  if n[3] != -1:
    neighbors[n[3]][0] = n[0]
    n_check.add(n[3])




T = int(input())
for case in range(1, T+1):
  result = 0
  R, C = [int(x) for x in input().split()]
  
  skills = []
  neighbors = []
  for _ in range(R):
    s = [int(x) for x in input().split()]
    skills.extend(s)

  for i in range(len(skills)):
    n = find_neighbors(i, R, C)
    neighbors.append(n)

  total = sum(skills)
  check = list(range(len(skills)))
  while True:
    remove = []
    result += total
    for i in check:
      if skills[i] != 0:
        if should_remove(i, skills, neighbors):
          remove.append(i)

    if len(remove) == 0:
      break

    n_check = set()
    for i in remove:
      total -= skills[i]
      skills[i] = 0
      change_neighbors(i, neighbors, n_check)
    check = list(n_check)


  print("Case #%d: %d" % (case, result))