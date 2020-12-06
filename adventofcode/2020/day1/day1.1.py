import sys

all_numbers = set(map(int, sys.stdin.read().split()))

for i in all_numbers:
  if 2020 - i in all_numbers:
    print(i * (2020 - i))
    break
