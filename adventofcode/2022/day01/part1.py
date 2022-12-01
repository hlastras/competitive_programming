import sys
lines = sys.stdin.read().split("\n")

best = 0
current = 0
for line in lines:
    if line == "":
        best = max(current, best)
        current = 0
    else:
        current += int(line)
if current != 0:
    best = max(current, best)

print(best)