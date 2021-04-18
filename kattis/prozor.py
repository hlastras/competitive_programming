from sys import stdin, stdout 
def to_int(cell):
  if cell == ".":
    return 0
  return 1

nr, ns, k = map(int, stdin.readline().split())
k -= 2
matrix_original = []
matrix_acc = []

for _ in range(nr):
  row = list(stdin.readline()[:ns])
  matrix_original.append(row)
  matrix_acc.append(list(map(to_int, row)))


best_r = -1
best_c = -1
best = -1
for r in range(nr-1):
  for c in range(ns-1):
    if r > 0:
      matrix_acc[r][c] += matrix_acc[r-1][c]
    if c > 0:
      matrix_acc[r][c] += matrix_acc[r][c-1]
    if r > 0 and c > 0:
      matrix_acc[r][c] -= matrix_acc[r-1][c-1]
    
    if r >= k and c >= k:
      t = matrix_acc[r][c]
      if r >= k:
        t -= matrix_acc[r-k][c]
      if c >= k:
        t -= matrix_acc[r][c-k]
      if r >= k and c >= k:
        t += matrix_acc[r-k][c-k]
      if t > best:
        best = t
        best_c = c
        best_r = r


a = [best_r - k, best_c - k]
b = [best_r - k, best_c + 1]
c = [best_r + 1, best_c - k]
d = [best_r + 1, best_c + 1]
matrix_original[a[0]][a[1]] = '+'
matrix_original[b[0]][b[1]] = '+'
matrix_original[c[0]][c[1]] = '+'
matrix_original[d[0]][d[1]] = '+'

for i in range(1, k+1):
  matrix_original[a[0]][a[1]+i] = '-'
  matrix_original[c[0]][c[1]+i] = '-'
  matrix_original[a[0]+i][a[1]] = '|'
  matrix_original[b[0]+i][b[1]] = '|'



stdout.write("%d\n" % best)
for r in matrix_original:
  stdout.write("%s\n" % "".join(r))