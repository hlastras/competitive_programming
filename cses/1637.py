n = int(input())
steps = 0

while n > 0:
  v = max([int(x) for x in str(n)])
  n -= v
  steps += 1

print(steps)