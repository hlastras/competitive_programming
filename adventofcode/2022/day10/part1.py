import sys
lines = sys.stdin.read().split("\n")

to_check = [20,60,100,140,180,220]
n = 0
x = 1
cycle = 0
total = 0
for line in lines:
    if line == "noop":
        cycle += 1
    else:
        _, value = line.split()
        value = int(value)

        if n<len(to_check) and cycle + 2 > to_check[n]-1:
            total += x*to_check[n]
            n += 1
        cycle += 2
        x += value
print(total)