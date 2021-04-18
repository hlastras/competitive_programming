import sys

lines = sys.stdin.read().strip().split("\n")
height = len(lines)
width = len(lines[0])

slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]

total = 1
for right, down in slopes:
  h = 0
  w = 0
  current = 0
  while h < height:
    if lines[h][w] == "#":
      current += 1
    h += down
    w = (w+right) % width

  total *= current

print(total)