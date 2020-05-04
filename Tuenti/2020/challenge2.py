from collections import defaultdict

c = int(input())

for case in range(1, c+1):
  m = int(input())
  skills = defaultdict(lambda: 0)
  for _ in range(m):
    a, b, win = [int(x) for x in input().split()]
    if win == 1 and skills[a] <= skills[b]:
      skills[a] = skills[b] + 1
    elif win == 0 and skills[b] <= skills[a]:
      skills[b] = skills[a] + 1
  
  result =  max(skills.items(), key=lambda x: x[1])[0]

  print("Case #%d: %d" % (case, result))