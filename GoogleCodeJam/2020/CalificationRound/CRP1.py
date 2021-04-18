T = int(input())

for case in range(T):
  N = int(input())
  matrix = []
  k = 0
  r = 0
  c = 0

  for i in range(N):
    l = [int(x) for x in input().split()]
    k += l[i]
    if len(set(l)) < N:
      r += 1
    matrix.append(l)

  for i in range(N):
    s = set()
    for j in range(N):
      s.add(matrix[j][i])

    if len(s) < N:
      c += 1
    
  print("Case #%d: %d %d %d" % (case+1, k ,r ,c))