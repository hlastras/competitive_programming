n = int(input())
matrix = []
for _ in range(n):
  matrix.append(list(map(lambda x: 1 if x == "." else 0, list(input()))))
  
for i in range(1,n):
  if matrix[0][i] == 1:
    matrix[0][i] = matrix[0][i-1]
  if matrix[i][0] == 1:
    matrix[i][0] = matrix[i-1][0]

for r in range(1, n):
  for c in range(1, n):
    if matrix[r][c] == 1:
      matrix[r][c] = (matrix[r-1][c] + matrix[r][c-1]) % 1000000007

print(matrix[n-1][n-1])