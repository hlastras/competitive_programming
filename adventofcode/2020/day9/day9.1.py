import sys

numbers = list(map(int, sys.stdin.read().strip().split("\n")))

t = 100

for i in range(t, len(numbers)):
  value = numbers[i]
  found = False
  for x in range(i-t, i):
    for y in range(x+1, x+t):
      if numbers[x] + numbers[y] == value:
        found = True

  if not found:
    print(value)
    break
