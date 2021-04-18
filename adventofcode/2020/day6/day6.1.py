import sys

lines = sys.stdin.read().strip().split("\n\n")

total = 0
for line in lines:
  line = line.replace("\n", "")
  total += len(set(list(line)))
print(total)