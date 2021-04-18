from sys import stdin, stdout
from math import sqrt

data_case = stdin.readline()
while data_case != "":
  
  n, l, w = map(int, data_case.split())
  data = []
  for _ in range(n):
    x, r = map(int, stdin.readline().split())
    if r*2 >= w:
      dx = sqrt(r**2 - (w/2)**2)
      if dx > 0:
        data.append([x-dx, x+dx])
  data.sort(key = lambda x: x[1], reverse=True)
  data.sort(key = lambda x: x[0])

  total = 0
  a = []
  end = 0
  # print(data)
  if len(data) > 0 and data[0][0] <= 0:
    for cs, ce in data:
      if ce > end:
        if cs > end:
          total = -1
          break
        else:
          if len(a) == 0:
            a.append([cs, ce])
            end = ce
            total += 1
          elif len(a) == 1:
            if cs <= 0 and cs > a[0][0]:
              a[-1] = [cs, ce]
              end = ce
            else:
              a.append([cs, ce])
              end = ce
              total += 1
          else:
            if cs <= a[-2][1]:
              a[-1] = [cs, ce]
              end = ce
            else:
              a.append([cs, ce])
              end = ce
              total += 1
      if end >= l:
        break
  if len(a) == 0 or a[0][0] > 0 or a[-1][1] < l:
    total = -1

  data_case = stdin.readline()
  stdout.write("%d\n" % total)

