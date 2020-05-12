a, b = [int(x) for x in input().split()]

if a == b:
  print(0)
else:
  if a > b:
    a,b = b,a

  matrix = [[0] * b for _ in range(a)]
  count = 0
  for i in range(a):
    matrix[i][0] = count
    count += 1
  count = 0
  for i in range(b):
    matrix[0][i] = count
    count += 1

  for row in range(1, a):
    for col in range(1, b):
      if col > row:
        best = 1000000000
        for x in range((col // 2)+1):
          best = min(best, matrix[row][x]+matrix[row][col-x-1]+1)
        for x in range((row // 2)+1):
          best = min(best, matrix[x][col]+matrix[row-x-1][col]+1)
        matrix[row][col] = best
        if row < b and col < a:
          matrix[col][row] = best

  print(matrix[-1][-1])