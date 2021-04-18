import sys

lines = sys.stdin.read().split("\n")
lcount = 0

cases = int(lines[lcount])
lcount += 1

for _ in range(cases):
  
  lcount += 2
  arr = [int(x) for x in lines[lcount].split()]
  lcount += 1
  accarr = []
  farr = []

  indexs = {}
  total = 0
  for i, x in enumerate(arr):
    total += x
    accarr.append(total)
    farr.append(total - 47)
    if total not in indexs:
      indexs[total] = []
    indexs[total].append(i)


  total = 0
  for i, x in enumerate(farr):
    if x in indexs:
      for v in indexs[x]:
        if v < i:
          total += 1
    elif x == 0:
      total += 1

    
  print(total)

