n, m = map(int, input().split())

matrix = []
matrix.append([0]*(m+2))
for _ in range(n):
  z = list(map(lambda x: 1 if x == "." else 0, input()))
  z.insert(0,0)
  z.append(0)
  matrix.append(z)

matrix.append([0]*(m+2))

# for row in matrix:
#   print(row)

count = 0
for row in range(1,n):
  for col in range(1,m):
    if matrix[row][col] == 1:
      count += 1
      queue = [(row, col)]
      while len(queue) > 0:
        r, c = queue.pop(0)
        if matrix[r][c] == 1:
          matrix[r][c] = 0
          if matrix[r-1][c] == 1:
            queue.append((r-1, c))
          if matrix[r+1][c] == 1:
            queue.append((r+1, c))
          if matrix[r][c-1] == 1:
            queue.append((r, c-1))
          if matrix[r][c+1] == 1:
            queue.append((r, c+1))

print(count)

