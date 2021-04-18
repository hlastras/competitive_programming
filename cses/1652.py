from sys import stdin, stdout
n, q = map(int, stdin.readline().split())
matrix = []
for _ in range(n):
  matrix.append(list(map(lambda x: 0 if x=="." else 1, stdin.readline()[:-1])))

for i in range(1,n):
  matrix[0][i] += matrix[0][i-1]
  matrix[i][0] += matrix[i-1][0]

for i in range(1,n):
  for j in range(1,n):
    matrix[i][j] += matrix[i-1][j] + matrix[i][j-1] - matrix[i-1][j-1]

for _ in range(q):
  r1, c1, r2, c2 = map(lambda x: int(x)-1, stdin.readline().split())

  s = matrix[r2][c2]
  if r1 > 0:
    s -= matrix[r1-1][c2]
  if c1 > 0:
    s -= matrix[r2][c1-1]
  if r1 > 0 and c1 > 0:
    s += matrix[r1-1][c1-1]
    
  stdout.write("%d\n" % (s))
