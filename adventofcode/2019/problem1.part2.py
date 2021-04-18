import sys
import math
lines = sys.stdin.read().split("\n")
total = 0
for l in lines:
  z = (int(l) // 3) - 2
  while z > 0:
    total += z
    z = (z // 3) - 2
print(total)