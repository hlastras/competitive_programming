n = int(input())
numbers = [int(x) for x in input().split()]

matrix = [[0] * n for _ in range(n)]

# Fill matrix in diagonals
for i in range(1, n):
  for j in range(n-i):
    k = j+i
    matrix[j][k] = max(matrix[k-1][j] + numbers[k], matrix[k][j+1] + numbers[j])
    matrix[k][j] = min(matrix[j][k-1], matrix[j+1][k])

print(matrix[0][-1])