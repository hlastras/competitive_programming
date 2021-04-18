import sys
lines = sys.stdin.read().split("\n")
lines.reverse()

def take(value, one, two, out):
  if one == 0:
    out.append("MOVE 2->1 %d" % two)
    one = two
    two = 0

  t = min(value, one)
  out.append("TAKE 1 %d" % t)
  one -= t
  if (value-t) > 0:
    return take((value-t), one, two, out)
  return one, two
    

out = []
orders = int(lines.pop())
while orders > 0:
  one = 0
  two = 0
  for _ in range(orders):
    action, value = lines.pop().split()
    value = int(value)

    if action == "TAKE":
      one, two = take(value, one, two, out)
    else:
      out.append("DROP 2 %d" % value)
      two += value
  
  
  orders = int(lines.pop())
  if orders != 0:
    out.append("")

print("\n".join(out))