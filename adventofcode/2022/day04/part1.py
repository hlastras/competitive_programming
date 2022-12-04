import sys
lines = sys.stdin.read().split("\n")

total = 0
for line in lines:
    elf1, elf2 = line.split(",")
    x1, y1 = [int(x) for x in elf1.split('-')]
    x1, y2 = [int(x) for x in elf2.split('-')]

    if (x1 >= x1 and y1 <= y2) or (x1 >= x1 and y2 <= y1):
        total += 1

print(total)
