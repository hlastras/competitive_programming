import math
import operator
from sys import stdin
lines = stdin.read().split("\n")[:-1]
lines.reverse()

ps = 6 / 99
pq = 6 / 9999
p = []
for i in range(100):
  row = []
  for j in range(10000):
    s = -3 + i * ps
    q = -3 + j * pq

    row.append(1 / (1+(math.e)**(-(s-q))))
  p.append(row)

cases = int(lines.pop())
prob = int(lines.pop())

for case in range(1, cases+1):
  
  matrix = []
  for _ in range(100):
    matrix.append(list(lines.pop()))

  mapping = {}
  for i, row in enumerate(matrix):
    mapping[row.count('1')] = i

  matrix.sort(key=lambda x: x.count('1'))
  matrix = [*zip(*matrix)]
  matrix.sort(key=lambda x: x.count('1'))
  matrix = [*zip(*matrix)]

  # ps = 6 / 99
  # pq = 6 / 9999

  hec = {}
  for i in range(100):
    hec[i] = 0

  for i, row in enumerate(matrix):
    for j, col in enumerate(row):
      # s = -3 + i * ps
      # q = -3 + j * pq

      # p = (1 / (1+(math.e)**(-(s-q))))
      hec[i] += abs(int(col)-p[i][j])

  res = min(hec.items(), key=operator.itemgetter(1))[0]
  res = mapping[matrix[res].count('1')]
  print(f'Case #{str(case)}: {str(res+1)}')