n = int(input())
for case in range(1, n+1):
  data = [int(x) for x in input().split()]
  target = data[0]
  forbidden = set(data[1:])
  numbers = list(filter(lambda x: x not in forbidden, range(1, target)))

  x = [0] * (target+1)
  x[0] = 1
  for val in numbers:
    for i in range(len(x)-val):
      if x[i] > 0:
        x[i+val] += x[i]

  print("Case #%d: %s" % (case, x[target]))