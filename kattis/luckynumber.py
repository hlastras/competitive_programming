n = int(input())


tot = 0
numbers = []

for n in range(2, 1001):
  tot = 0
  def r(acc, l, end):
    if acc % l != 0:
      return 
    if l == end:
      global tot
      tot += 1
      return

    for x in range(10):
      r(acc*10+x, l+1, end)

    return

  for i in range(1, 10):
    res = r(i, 1, n)

  print(tot)