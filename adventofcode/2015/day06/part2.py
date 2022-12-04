import re
import sys
lines = sys.stdin.read().split("\n")

exp = r"^(turn on|turn off|toggle)\s(\d+),(\d+)\sthrough\s(\d+),(\d+)$"
def parse(line):
    r = re.findall(exp, line)
    acction, x1, y1, x2, y2 = r[0]
    return acction , [int(x1), int(y1)], [int(x2), int(y2)]

matrix = [[0 for j in range(1000)] for i in range(1000)]

for line in lines:
    action, f, t = parse(line)
    for i in range(f[0],t[0]+1):
        for j in range(f[1],t[1]+1):
            if action == "turn on":
                matrix[i][j] += 1
            elif action == "turn off":
                if matrix[i][j] > 0:
                    matrix[i][j] -= 1
            else:
                matrix[i][j] += 2


total = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        total += matrix[i][j]

print(total)