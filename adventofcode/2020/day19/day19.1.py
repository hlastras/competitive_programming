import sys
regex_rule = r'(\d+): (.+)'
a = """0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb
"""
# lines = a.split("\n\n")
lines = sys.stdin.read().strip().split("\n\n")

r, p = lines[0].split("\n"), lines[1].split("\n")
rules = {}
patterns = {}
for rule in r:
  i = rule.find(":")
  position = int(rule[:i])
  rule = rule[i+2:].split(" | ")
  rules[position] = rule

print(rules)

def solve(index):
  if index in patterns:
    return patterns[index]
  else:
    rule = rules[index]
    if rule[0].startswith("\""):
      value = rule[0].replace("\"", "")
      patterns[index] = [value]
      return [value]
    else:
      s = []
      for v in rule:
        v = list(map(int, v.split(" ")))
        z = []
        for i in v:
          z.append(solve(i))
        rec("", z, s)
      patterns[index] = s
      return s

def rec(acc, l, s):
  # print(acc)
  # print(l)
  if len(l) > 1:
    for suf in l[0]:
      # print(acc, suf)
      rec(acc+suf, l[1:], s)
  elif len(l) == 1:
    for suf in l[0]:
      rec(acc+suf, [], s)
  else:
    s.append(acc)



sol = set(solve(0))
# print(sol)
total = 0
for line in p:
  if line in sol:
    total += 1
print(total)