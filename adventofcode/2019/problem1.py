import sys
import math
lines = sys.stdin.read().split("\n")
total = 0
for l in lines:
  total += (int(l) // 3) - 2
print(total)