import sys

tiles = sys.stdin.read().strip().split("\n\n")

up = []
right = []
down = []
left = []
tiles_values = {}

for tile in tiles:
  lines = tile.split("\n")
  id = int(lines[0][5:9])
  lines = lines[1:]
  values = []
  # up
  n = ""
  for i in range(len(lines[0])):
    if lines[0][i] == "#":
      n += "1"
    else:
      n += "0"
  value = int(n, 2)
  values.append(value)
  up.append(value)
  print(id, value, n)

  # right
  n = ""
  for i in range(len(lines)):
    if lines[i][-1] == "#":
      n += "1"
    else:
      n += "0"
  value = int(n, 2)
  values.append(value)
  right.append(value)

  # down
  n = ""
  for i in range(len(lines[-1])):
    if lines[-1][i] == "#":
      n += "1"
    else:
      n += "0"
  value = int(n, 2)
  values.append(value)
  down.append(value)
  print(id, value, n)

  # left
  n = ""
  for i in range(len(lines)):
    if lines[i][0] == "#":
      n += "1"
    else:
      n += "0"
  value = int(n, 2)
  values.append(value)
  left.append(value)

  tiles_values[id] = values

print(up)
print(down)
print()
print()
# print(tiles_values)
print()
print()

print(up.difference(down))
print(down.difference(up))
print(left.difference(right))
print(right.difference(left))