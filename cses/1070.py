n = int(input())

if n != 2 and n != 3:
  res = list(range(2, n+1, 2))
  res.extend(range(1, n+1, 2))
  print(" ".join(str(x) for x in res))
else:
  print("NO SOLUTION")
