import sys
lines = sys.stdin.read().split("\n")

groups = zip(*[iter(lines)] * 3)

total = 0
for group in groups:
    badge = set(group[0]) & set(group[1]) & set(group[2])

    value = ord(badge.pop())
    if value < 91:
        # is uppercase
        value -= 38
    else:
        # is downcase
        value -= 96

    total += value

print(total)