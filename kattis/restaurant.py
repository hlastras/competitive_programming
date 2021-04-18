def take(value, one, two):
  if one[0] == 0:
    print("MOVE 2->1 %d" % two[0])
    one[0] = two[0]
    two[0] = 0

  t = min(value, one[0])
  print("TAKE 1 %d" % t)
  one[0] -= t
  if (value-t) > 0:
    take((value-t), one, two)
    

def drop(value, one, two):
  print("DROP 2 %d" % (value))
  two[0] += value


orders = int(input())
drops = 0
while orders > 0:
  one = [0]
  two = [0]
  for _ in range(orders):
    action, value = input().split()
    value = int(value)

    if action == "TAKE":
      take(value, one, two)
    else:
      drop(value, one, two)
  
  
  orders = int(input())
  if orders != 0:
    print()