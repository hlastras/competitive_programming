def median(sub):
  print(" ".join(map(str, sub)))
  m = int(input())
  if m == -1:
    exit(0)
  return sub.index(m)

def solve(a):
  print(" ".join(map(str, a)))
  m = int(input())
t, n, q = [int(x) for x in input().split()]

for _ in range(t):
  s = []
  c = [1, 2, 3]
  m = median(c)
  s.append(c[(m-1)%3])
  s.append(c[m])
  s.append(c[(m+1)%3])


  for i in range(4, n+1):
    s.append(i)
    index = i

    should_end = False
    while True:
      m = median(s[index-3:index])
      if m == 0:
        # pasar al principio y deslizas
        s[index-1], s[index-2], s[index-3] = s[index-2], s[index-3], s[index-1]
        index -= 2
      elif m == 1:
        # Colocado, terminar
        break
      else:
        # Mover al centro y terminar
        s[index-1], s[index-2] = s[index-2], s[index-1]
        break

      if index < 3:
        if index == 2:
          should_end = True
        break

    if should_end:
      m = median(s[:3])
      if m == 0:
        s[0], s[1] = s[1], s[0]
    
  solve(s)
