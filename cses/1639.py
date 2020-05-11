a = input()
b = input()
la = len(a)+1
lb = len(b)+1

matrix = [[0] * lb for _ in range(la)]
count = 0
for i in range(max(la, lb)):
  if i < la:
    matrix[i][0] = count
  if i < lb:
    matrix[0][i] = count
  count += 1

for r in range(1, la):
  for c in range(1, lb):
    matrix[r][c] = min(matrix[r][c-1]+1, matrix[r-1][c]+1, matrix[r-1][c-1] + (0 if a[r-1]==b[c-1] else 1))

print(matrix[-1][-1])