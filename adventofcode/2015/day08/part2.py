import re
import sys
lines = sys.stdin.read().split("\n")

total = 0
for line in lines:
    r = re.findall(r'(\\)', line)
    total += len(r)
    r = re.findall(r'(")', line)
    total += len(r)

    total += 2
print(total)