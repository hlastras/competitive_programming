import math

T = int(input())

for case in range(1, T+1):

  N, K = [int(x) for x in input().split()]
  valid = True
  if N == 3 and K in [4,5,7,8]:
    valid = False
  elif K == (N+1) or K == ((N*N)-1):
    valid = False

  if valid:
    print("Case #%d: POSSIBLE" % case)
  else:
    print("Case #%d: IMPOSSIBLE" % case)
    continue

  end = False
  listado = []

  def is_valid(listado):
    if len(set(listado)) == 2:
      m = {}
      for v in listado:
        if v not in m:
          m[v] = 0
        m[v] += 1
      for k in m.keys():
        if m[k] == 1:
          return False
    return True

  def rec(obj, ob, max, lista, sum):
    global end
    if end:
      return
    if len(lista) == max:
      global listado
      if sum == ob and is_valid(listado):
        for x in lista:
          listado.append(x)
        end = True
      return
    if obj <= 0:
      return

    next = int(math.sqrt(obj))
    lista.append(next)
    rec(obj-next, ob, max, lista, sum+next)
    lista.pop()
    if obj-max >= 0:
      lista.append(max)
      rec(obj-max, ob, max, lista, sum+max)
      lista.pop()

  # print(len([31, 31, 30, 30, 29, 29, 28, 28, 27, 27, 26, 26, 25, 25, 24, 24, 23, 50, 50, 20, 20, 50, 18, 18, 17, 17, 50, 15, 50, 12, 12, 50, 9, 8, 8, 7, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]))
  rec(K, K, N, [], 0)

  matrix = []
  for _ in range(N):
    matrix.append([-1] * N)

  for i, val in enumerate(listado):
    matrix[i][i]= val



  def can_add(v, row, col, matrix):
    # check row
    if v in matrix[row]:
      return False
    # check column
    for r in range(len(matrix)):
      if matrix[r][col] == v:
        return False

    return True

  def decompose(pos, N):
    row = pos // N
    col = pos % N
    return row, col

  def recur(pos, matrix, N):
    if pos == (N*N)-1:
      return matrix

    row, col = decompose(pos, N)

    if matrix[row][col] != -1:
      res = recur(pos + 1, matrix, N)
      if res:
        return res
    else:
      for v in range(1, N+1):
        if can_add(v, row, col, matrix):
          matrix[row][col] = v
          res = recur(pos + 1, matrix, N)
          if res:
            return res
          matrix[row][col] = -1
    return

  res = recur(0, matrix, N)

  for row in res:
    print(" ".join([str(x) for x in row]))
