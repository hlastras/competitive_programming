import math
cases = int(input())
print(cases)

for i in range(cases):
  message = input()

  l = len(message)
  m = math.ceil(math.sqrt(l))

  matrix = [['*'] * m for _ in range(m)]
  c = 0
  for row in range(m):
    for col in range(m):
      if c < l:
        matrix[row][col] = message[c]
        c += 1
      else:
        break

  result = []
  for col in range(m):
    for row in reversed(range(m)):
      if matrix[row][col] != '*':
        result.append(matrix[row][col])
  print("".join(result))