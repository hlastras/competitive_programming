import sys

numbers = list(map(int, sys.stdin.read().strip().split("\n")))

numbers.append(0)
numbers.sort()
numbers.append(numbers[-1] + 3)

prev = numbers[0]
one = 0
three = 0
for n in numbers[1:]:
  diff = n - prev
  if diff == 1:
    one += 1
  elif diff == 3:
    three += 1

  prev = n

print(one * three)