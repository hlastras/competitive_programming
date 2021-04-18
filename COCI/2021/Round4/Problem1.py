import sys
lines = sys.stdin.read().strip().split("\n")

disagree_toppings = set(map(int, lines[0].split(" ")[1:]))

result = 0
for line in lines[2:]:
  toppings = set(map(int, line.split(" ")[1:]))

  if len(toppings.intersection(disagree_toppings)) == 0:
    result += 1

print(result)