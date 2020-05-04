n = int(input())

for i in range(1, n+1):
  result = "-"
  s = set(input().split())
  if "R" in s and "S" in s:
    result = "R"
  elif "R" in s and "P" in s:
    result = "P"
  elif "S" in s and "P" in s:
    result = "S"

  print("Case #%d: %s" % (i, result))