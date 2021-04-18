from sys import stdin, stdout 

T = int(stdin.readline())
for _ in range(T):
  m, c = map(int, stdin.readline().split())

  s = set([0])
  for i in range(c):
    vals = list(map(int, stdin.readline().split()))[1:]
    ns = set()
    for v in vals:
      for v2 in s:
        if (v+v2) <= m:
          ns.add(v+v2)
    s = ns

  if len(s) > 0:
    stdout.write("%d\n" % max(s))
  else:
    stdout.write("no solution\n")
