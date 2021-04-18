import sys
import math
lines = sys.stdin.read().strip().split("\n")

for line in lines[1:]:
  a, b, c, d = list(map(int, line.split(" ")))

  y = 1
  for i in range(a, b+1):
    y *= i

  z = 1
  for i in range(c, d+1):
    z *= i

  if z % y == 0:
    print("DA")
  else:
    print("NE")
