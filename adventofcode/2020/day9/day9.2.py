import sys

numbers = list(map(int, sys.stdin.read().strip().split("\n")))
target = 25918798
# target = 127

acc = [numbers[0]]
for n in numbers[1:]:
  acc.append(n+acc[-1])

end = False
for x in range(len(acc)):
  for y in range(x-1, len(acc)):
    if acc[y] - acc[x] == target:
      print(min(numbers[x:y])+max(numbers[x:y]))
      end = True
      break

  if end:
    break