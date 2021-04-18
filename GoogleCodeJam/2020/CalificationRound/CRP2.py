T = int(input())

for case in range(T):
  result = ""
  S = input()
  stack = []
  deep = 0
  for c in S:
    value = int(c)
    diff = value - deep
    if diff > 0:
      result += "(" * diff
      result += c
    elif diff < 0:
      result += ")" * abs(diff)
      result += c
    else:
      result += c
    
    deep += diff
  result += ")" * deep

    
  print("Case #%d: %s" % (case+1, result))