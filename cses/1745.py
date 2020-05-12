input()
numbers = [int(x) for x in input().split()]

seen = [False] * (sum(numbers)+1)
seen[0] = True

for num in numbers:
  for i in range(len(seen)-1, num-1, -1):
    if seen[i-num]:
      seen[i] = True

count = 0
result = []
for i in range(1, len(seen)):
  if seen[i]:
    count += 1
    result.append(i)

print(count)
print(" ".join(str(x) for x in result))