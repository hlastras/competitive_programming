import sys
from copy import deepcopy

def get_value(matrix, row, col):
  if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
    return "-"
  return matrix[row][col]

def count_adjacents_occupied(matrix, row, col):
  total = 0
  m = max(len(matrix), len(matrix[0]))
  # up
  for i in range(row-1, -1, -1):
    if matrix[i][col] == "#":
      total += 1
      break
    if matrix[i][col] == "L":
      break
  # up right
  for i in range(1,m):
    v = get_value(matrix, row-i, col+i)
    if v == "-" or v == "L":
      break
    if v == "#":
      total += 1
      break
  # right
  for i in range(col+1, len(matrix[0])):
    if matrix[row][i] == "#":
      total += 1
      break
    if matrix[row][i] == "L":
      break
  # down right
  for i in range(1,m):
    v = get_value(matrix, row+i, col+i)
    if v == "-" or v == "L":
      break
    if v == "#":
      total += 1
      break
  # down
  for i in range(row+1, len(matrix)):
    if matrix[i][col] == "#":
      total += 1
      break
    if matrix[i][col] == "L":
      break
  # down left
  for i in range(1,m):
    v = get_value(matrix, row+i, col-i)
    if v == "-" or v == "L":
      break
    if v == "#":
      total += 1
      break
  # left
  for i in range(col-1, -1, -1):
    if matrix[row][i] == "#":
      total += 1
      break
    if matrix[row][i] == "L":
      break
  # up left
  for i in range(1,m):
    v = get_value(matrix, row-i, col-i)
    if v == "-" or v == "L":
      break
    if v == "#":
      total += 1
      break



  # for r in range(row-1, row+2):
  #   for c in range(col-1, col+2):
  #     if r != row or c != col:
  #       if get_value(matrix, r, c) == "#":
  #         total += 1
  return total



ferry = list((map(list, sys.stdin.read().strip().split("\n"))))
old_ferry = deepcopy(ferry)

has_changes = True
while has_changes:
  has_changes = False
  for r in range(len(old_ferry)):
    for c in range(len(old_ferry[0])):
      if old_ferry[r][c] == "L":
        ad = count_adjacents_occupied(old_ferry, r, c)
        if ad == 0:
          ferry[r][c] = "#"
          has_changes = True
      elif old_ferry[r][c] == "#":
        ad = count_adjacents_occupied(old_ferry, r, c)
        if ad >= 5:
          ferry[r][c] = "L"
          has_changes = True

  old_ferry = ferry
  ferry = deepcopy(old_ferry)


total = 0
for row in ferry:
  for c in row:
    if c == "#":
      total += 1
print(total)

