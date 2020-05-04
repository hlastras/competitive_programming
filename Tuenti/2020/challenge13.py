n = int(input())
for case in range(1, n+1):

  available = int(input())
  best_height = -1
  best_use = -1

  init = 1
  while True:
    acc1 = ((init+4)**2)*2 - (init+2)**2 + (init**2)*2
    acc2 = ((init+4)*(init+5))*2 - (init+2)*(init+3) + (init*(init+1))*2
    height = 3
    x = init + 4

    while acc1 <= available or acc2 <= available:
      if height >= best_height:
        if acc1 <= available and acc2 > available:
          best_use = acc1
          best_height = height
        elif acc2 <= available and acc1 > available:
          best_use = acc2
          best_height = height
        elif acc1 <= available and acc2 <= available:
          best_use = max(acc1, acc2)
          best_height = height
        else:
          break
      height += 1
      x += 4
      acc1 += ((x**2) + (x-1)*4)
      acc2 += ((x*(x+1)) + (x-1)*4) + 2

    init += 1

    if height == 3 or height < best_height:
      break

  if best_height >= 3:
    print("Case #%d: %d %d" % (case, best_height, best_use))
  else:
    print("Case #%d: IMPOSSIBLE" % case)
