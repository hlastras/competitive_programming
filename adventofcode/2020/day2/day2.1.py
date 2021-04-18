import re
import sys

lines = sys.stdin.read().strip().split("\n")

great = 0
for line in lines:
  match = re.match("(\d+)-(\d+) (\w): (\w+)", line)
  
  minimum = int(match.group(1))
  maximum = int(match.group(2))
  character = match.group(3)
  password = match.group(4)
  
  counts = {}
  for c in password:
    if c in counts:
      counts[c] += 1
    else:
      counts[c] = 1

  counter = 0
  if character in counts:
    counter = counts[character]

  if counter >= minimum and counter <= maximum:
    great += 1

print(great)