n = int(input())

for case in range(1, n+1):
  number = int(input())
  result = "IMPOSSIBLE"
  if (number % 20) <= (number // 20) * 9:
    result = str(number // 20)

  print("Case #%d: %s" % (case, result))