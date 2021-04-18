def quadrant(n, x1, y1):
  if n == 1:
    return 1

  mid = n // 2
  if x1 < mid:
    if y1 < mid:
      return quadrant(mid, x1, y1)
    else:
      return quadrant(mid, x1, y1-mid)
  else: 
    if y1 < mid:
      return quadrant(mid, x1-mid, y1)
    else:
      return -1 * quadrant(mid, x1-mid, y1-mid)


cases = int(input())
for _ in range(cases):
  n, x, y, w, h = [int(x) for x in input().split()]

  for x1 in range(y, y+h):
    line = []
    for y1 in range(x, x+w):
      line.append(str(quadrant(n, x1, y1)))
    print(" ".join(line))

  print()