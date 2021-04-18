import re
import sys
re_ranges = r'[\w ]+: (\d+-\d+) or (\d+-\d+)'
ranges, ticket, nearby = sys.stdin.read().strip().split("\n\n")

values = set()
for r in ranges.split("\n"):
  match =  match = re.search(re_ranges, r)
  range1 = match.group(1).split("-")
  range2 = match.group(2).split("-")

  values = values.union(list(range(int(range1[0]), int(range1[1]))))
  values = values.union(list(range(int(range2[0]), int(range2[1]))))

total = 0
for n in nearby.split("\n")[1:]:
  nearby_ticket_values = list(map(int, n.split(",")))
  for v in nearby_ticket_values:
    if v not in values:
      total += v

print(total) 