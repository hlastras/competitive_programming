import math
cases = int(input())
for case in range(1, cases+1):
  prob = int(input())

  matrix = []
  for _ in range(100):
    # matrix.append(list(input()))
    matrix.append(list(map(int, list(input()))))
    # print(matrix[-1].count(1))

  mapping = {}
  for i, row in enumerate(matrix):
    mapping[row.count(1)] = i

  # print(matrix[58].count(1))
  # print((matrix[1]))
  matrix.sort(key=lambda x: x.count(1))
  matrix = [*zip(*matrix)]
  matrix.sort(key=lambda x: x.count(1))
  matrix = [*zip(*matrix)]
  # for r in matrix:
  #   print(r.count(1))
  # print(matrix[-1])
  # print(matrix[-2])
  # print(matrix[-50])

  ps = 6 / 99
  pq = 6 / 9999

  hec = {}
  for i in range(100):
    hec[i] = 0
  # for i in range(10000):
  #   print(-3+i*pq)
  for i, row in enumerate(matrix):
    for j, col in enumerate(row):
      s = -3 + i * ps
      q = -3 + j * pq

      # if q-s in [-6.0, 6.0]:
      #   print(q, s, math.e**(q-s))
      #   print(1 / (1+(math.e)**(-(s-q))))
      p = (1 / (1+(math.e)**(-(s-q))))
      # if col == 1:
      hec[i] += abs(col-p)
      # elif p >= 0.5 and col == 0:
      #   hec[i] += 1
      # break
    # print(q, s)

  # print(hec)
  import operator
  # res = max(hec.items(), key=operator.itemgetter(1))[0]
  # print(matrix[res].count(1))
  # print(max(hec.items(), key=operator.itemgetter(1))[0])
  # print(min(hec.items(), key=operator.itemgetter(1))[0])

  # print(mapping)
  res = min(hec.items(), key=operator.itemgetter(1))[0]
  res = mapping[matrix[res].count(1)]
  print(f'Case #{str(case)}: {str(res+1)}')