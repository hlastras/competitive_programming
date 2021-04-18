import sys
from collections import defaultdict

tiles = sys.stdin.read().strip().split("\n\n")

tiles_values = defaultdict(list)

for tile in tiles:
  lines = tile.split("\n")
  id = int(lines[0][5:9])
  lines = lines[1:]
  # values = []
  # up
  n = ""
  for i in range(len(lines[0])):
    if lines[0][i] == "#":
      n += "1"
    else:
      n += "0"
  value1 = int(n, 2)
  value2 = int(n[::-1], 2)
  value = (value1 * value2) + (value1 + value2)
  tiles_values[value].append(id)
  print(id, value, value1, value2)


  # right
  n = ""
  for i in range(len(lines)):
    if lines[i][-1] == "#":
      n += "1"
    else:
      n += "0"
  value1 = int(n, 2)
  value2 = int(n[::-1], 2)
  value = (value1 * value2) + (value1 + value2)
  tiles_values[value].append(id)
  print(id, value, value1, value2)

  # down
  n = ""
  for i in range(len(lines[-1])):
    if lines[-1][i] == "#":
      n += "1"
    else:
      n += "0"
  value1 = int(n, 2)
  value2 = int(n[::-1], 2)
  value = (value1 * value2) + (value1 + value2)
  tiles_values[value].append(id)
  print(id, value, value1, value2)

  # left
  n = ""
  for i in range(len(lines)):
    if lines[i][0] == "#":
      n += "1"
    else:
      n += "0"
  value1 = int(n, 2)
  value2 = int(n[::-1], 2)
  value = (value1 * value2) + (value1 + value2)
  tiles_values[value].append(id)
  print(id, value, value1, value2)

corners = defaultdict(int)
for key in tiles_values:
  print(key, tiles_values[key])
  if len(tiles_values[key]) == 1:
    corners[tiles_values[key][0]] += 1

total = 1
for k in corners:
  if corners[k] == 2:
    total *= k

print(total)