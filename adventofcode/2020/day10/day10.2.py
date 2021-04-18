# For this solution we know input puzzle only have differences of 1 or 3, never 2
import sys

def calculate(length):
  if length <= 1:
    return 1
  elif length == 2:
    return 2
  else:
    return (3 * length) - 5 

numbers = list(map(int, sys.stdin.read().strip().split("\n")))
numbers.append(0)
numbers.sort()
numbers.append(numbers[-1] + 3)

total = 1
group_length = 0
for i in range(1, len(numbers)):
  if (numbers[i] - numbers[i-1]) == 1:
    group_length += 1
  else:
    total *= calculate(group_length)
    group_length = 0

print(total)