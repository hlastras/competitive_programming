from sys import stdin, stdout 

t, n = map(int, stdin.readline().split())

breaks = list(map(int, stdin.readline().split()))

matrix = []
for _ in range(n+1):
  row = [0] * (t+1)
  matrix.append(row)


for row in range(1, len(matrix)):
  value = breaks[row-1]
  for col in range(len(matrix[row])):
    if col < value:
      matrix[row][col] = matrix[row-1][col]
    else:
      matrix[row][col] = max(matrix[row-1][col], matrix[row-1][col-value]+value)


result = [0] * n
acc1 = 0
acc2 = 0
while col>0 or row>0:
  value = breaks[row-1]
  if matrix[row-1][col] != matrix[row][col]:
    result[row-1] = acc1
    acc1 += value
    col -= value
  else:
    result[row-1] = acc2
    acc2 += value
  row -= 1


stdout.write("%s\n" % " ".join([str(x) for x in result]))