from sys import stdin, stdout 
T = int(stdin.readline())

for case in range(1, T+1):
  stdin.readline() # Ignore n, we don't need that value
  va = sorted([int(x) for x in stdin.readline().split()])
  vb = sorted([int(x) for x in stdin.readline().split()], reverse=True)

  result = sum(a * b for a, b in zip(va, vb))

  stdout.write("Case #%d: %d\n" % (case, result))