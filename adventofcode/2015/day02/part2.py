import sys
lines = sys.stdin.read().split("\n")

total = 0
for line in lines:
    x1, x2, x3 = [int(x) for x in line.split("x")]
    total += min(x1+x2, x1+x3, x2+x3)*2 + x1*x2*x3
print(total)