import sys
import re
from collections import defaultdict

lines = sys.stdin.read().strip().split("\n")

rules = defaultdict(list)
for line in lines:
  outside_color, inside_colors_raw = line.split(" bags contain ", 1)
  for c in inside_colors_raw.split(", "):
    match = re.search(r'\d+ ([\w ]+) bag', c)
    if match:
      color = match.group(1)
      rules[color].append(outside_color)

seen = set()
queue = rules["shiny gold"]
while len(queue) > 0:
  next = queue.pop(0)
  queue.extend(rules[next])
  seen.add(next)

print(len(seen))
  
