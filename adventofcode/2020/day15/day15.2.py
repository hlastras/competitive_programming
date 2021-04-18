numbers = list(map(int, input().split(",")))

last_seen = {}

for i, v in enumerate(numbers[:-1]):
  last_seen[v] = i+1

last = numbers[-1]
for i in range(len(numbers), 30000000):
  if last in last_seen:
    next = i-last_seen[last]
  else:
    next = 0

  last_seen[last] = i
  last = next

print(last)
