import sys

all_numbers = list(map(int, sys.stdin.read().split()))

pairs = set()
for i in range(len(all_numbers)):
  for j in range(i+1, len(all_numbers)):
    pairs.add(all_numbers[i] + all_numbers[j])

numbers = []
total = 1
for n in all_numbers:
  if 2020 - n in pairs:
    total *= n

print(total)