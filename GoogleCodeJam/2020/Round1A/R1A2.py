T = int(input())

for case in range(1, T+1):
  N = int(input())
  acumulate = 0
  path = [[0, 1]]
  if N > 30:
    x = N - 30
    acumulate += x
    s = bin(x)[2:][::-1]
    for c in s:
      if c == '1':
        r = path[-1][0] + 1
        ran = range(1, r+1) if path[-1][1] == 1 else range(r, 0, -1)
        for k in ran:
          path.append([r, k])
      else:
        acumulate += 1
        k = 1 if path[-1][1] == 1 else (path[-1][1] + 1)
        path.append([path[-1][0] + 1, k])

  for _ in range(N - acumulate):
    k = 1 if path[-1][1] == 1 else (path[-1][1] + 1)
    path.append([path[-1][0] + 1, k])
  
  print("Case #%d:" % case)
  for p in path[1:]:
    print("%d %d" % (p[0], p[1]))