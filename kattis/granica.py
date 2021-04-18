c = int(input())
n = []
for _ in range(c):
  n.append(int(input()))

s = set()
while True:
  found = False
  for v in range(2, max(n)):
    all_eq = True
    x = n[0]%v
    for j in n:
      if j%v != x:
        all_eq = False
        break
    
    if all_eq:
      found = True
      news = []
      for i in s:
        news.append(i*v)
      for i in news:
        s.add(i)
      s.add(v)
      n = list(map(lambda x: int(x/v), n))
      break

  if not found:
    break

print(" ".join([str(x) for x in s]))