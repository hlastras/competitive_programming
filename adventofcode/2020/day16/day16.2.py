import re
import sys
re_ranges = r'([\w ]+): (\d+-\d+) or (\d+-\d+)'
ranges, ticket, nearby = sys.stdin.read().strip().split("\n\n")

rules_values = []
all_values = set()
for i, r in enumerate(ranges.split("\n")):
  v = set()
  match =  match = re.search(re_ranges, r)
  range1 = match.group(2).split("-")
  range2 = match.group(3).split("-")

  v = v.union(list(range(int(range1[0]), int(range1[1])+1)))
  v = v.union(list(range(int(range2[0]), int(range2[1])+1)))
  rules_values.append(v)
  all_values = all_values.union(v)


tickets_values = [set() for _ in range(len(rules_values))]




# for n in nearby.split("\n")[1:]:
#   ticket = list(map(int, n.split(",")))
#   is_ticket_valid = True
#   for i, field_value in enumerate(ticket):
#     if field_value not in all_values:
#       is_ticket_valid = False
#     else:
#       for j, v in enu:




# valid_tickets = []
for n in nearby.split("\n")[1:]:
  nearby_ticket_values = list(map(int, n.split(",")))
  is_ticket_valid = True
  for v in nearby_ticket_values:
    if v not in all_values:
      is_ticket_valid = False

  if is_ticket_valid:
    for i, v in enumerate(nearby_ticket_values):
      tickets_values[i].add(v)


hector = [list() for _ in range(20)]
for col_number, a in enumerate(tickets_values):
  for rule_number, b in enumerate(rules_values):
    if len(a.intersection(b)) == len(a):
      print("Columna "+str(col_number)+" regla "+str(rule_number))
      hector[col_number].append(rule_number)

ranges = ranges.split("\n")

hector = list(zip(range(len(hector)), hector))
hector = sorted(hector, key=lambda x: len(x[1]))

res = {}
my_ticket = list(map(int, ticket.split("\n")[1].split(",")))
total = 0
total2 = 0
while len(hector) > 0:
  hector = sorted(hector, key=lambda x: len(x[1]))
  # for r in hector:
  #   print(r)
  print()
  print()
  print()
  print()
  rule, values = hector.pop(0)
  if len(values) > 1:
    print("WRONG!!")
    exit(1)

  if values[0] < 6:
    print("------")
    print(rule, values, my_ticket[int(rule)])
    total += my_ticket[int(rule)]
    print("------")
  
  if rule < 6:
    print(">>>>>>")
    print(rule, values, my_ticket[values[0]])
    total2 += my_ticket[values[0]]
    print(">>>>>>")
  
  match =  match = re.search(re_ranges, ranges[values[0]])
  name = match.group(1)
  res[name] = rule

  for i in range(len(hector)):
    hector[i][1].remove(values[0])
print("TOTAL:", total, total2)

print(res)

print(my_ticket)
total = 0
for key in res:
  if key.startswith("departure"):
    col_num = res[key]
    print(key, col_num, my_ticket[col_num])
    total += my_ticket[col_num]

print(total)
  

  