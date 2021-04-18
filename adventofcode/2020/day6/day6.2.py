import sys

lines = sys.stdin.read().strip().split("\n\n")

total = 0
for line in lines:
  persons = line.split("\n")
  choices = list(map(set, list(persons)))
  
  base = choices[0]
  for c in choices[1:]:
    base = base.intersection(c)
  
  total += len(base)
print(total)