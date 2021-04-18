from functools import reduce
import re
import sys
re_ranges = r'([\w ]+): (\d+-\d+) or (\d+-\d+)'


def ruleToRange(rule):
  numbers = set()
  match =  match = re.search(re_ranges, rule)
  range1 = match.group(2).split("-")
  range2 = match.group(3).split("-")
  numbers = numbers.union(list(range(int(range1[0]), int(range1[1])+1)))
  numbers = numbers.union(list(range(int(range2[0]), int(range2[1])+1)))
  return numbers

def valid_ticket(ticket, all):
  for i, value in enumerate(ticket):
    if value not in all:
      return False
  return True

def join_nearby(acc, ticket):
  for i, value in enumerate(ticket):
    acc[i].add(value)
  return acc

def algo(range, values):
  ans = []
  for i, v in enumerate(values):
    if len(v.intersection(range)) == len(v):
      ans.append(i)
  return ans

ranges, ticket, nearby = sys.stdin.read().strip().split("\n\n")
ranges = ranges.split("\n")
ticket = ticket.split("\n")[1:]
ticket = list(map(int, ticket[0].split(",")))
nearby = nearby.split("\n")[1:]
nearby = list(map(lambda x: list(map(int, x.split(","))), nearby))


ranges = list(map(ruleToRange, ranges))
all = set()
for r in ranges:
  all = all.union(r)

nearby = list(filter(lambda x: valid_ticket(x, all), nearby))
values = [set() for _ in range(len(nearby[0]))]
values = reduce(lambda a,b: join_nearby(a, b), nearby, values)

a = list(map(lambda x: algo(x, values), ranges))
a = zip(range(len(a)), a)
a = sorted(a, key=lambda x: len(x[1]))

used = set()
total = 1
while len(a) > 0:
  line = a.pop(0)
  for i in used:
    line[1].remove(i)
  used.add(line[1][0])
  if line[0] < 6: #
    total *= ticket[line[1][0]]

print(total)