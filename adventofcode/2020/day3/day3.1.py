import sys

lines = sys.stdin.read().strip().split("\n")
height = len(lines)
width = len(lines[0])

h = 0
w = 0
total = 0
while h < height:
  if lines[h][w] == "#":
    total += 1
  h += 1
  w = (w+3) % width

print(total)