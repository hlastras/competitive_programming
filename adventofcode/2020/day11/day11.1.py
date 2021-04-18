import sys
from copy import deepcopy

def get_value(matrix, row, col):
  if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
    return "-"
  return matrix[row][col]

def count_adjacents_occupied(matrix, row, col):
  total = 0
  for r in range(row-1, row+2):
    for c in range(col-1, col+2):
      if r != row or c != col:
        if get_value(matrix, r, c) == "#":
          total += 1
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
        if ad >= 4:
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