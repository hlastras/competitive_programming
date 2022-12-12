import re
import sys
lines = sys.stdin.read().split("\n")

total = 0
for line in lines:
    total += len(line)
    line = line[1:-1]
    line = re.sub(r'\\x(\d|[a-f]){2}|\\"|\\\\', " ", line)
    total -= len(line)
print(total)