T = int(input())


d = ['W', 'S', 'E', 'N']

for case in range(1, T+1):
  result = ""

  x, y = map(int, input().split())
  rot = 0
  if x < 0 and y < 0:
    rot = 2
  elif x < 0:
    rot = 1
    x, y = y, x
  elif y < 0: 
    rot = 3
    x, y = y, x

  x = abs(x)
  y = abs(y)

  if (x+y) % 2 == 0 and (x != 0 or y != 0):
    result = "IMPOSSIBLE"
  else:
    while x != 0 or y != 0:
      if (x==0 and abs(y)==1) or (abs(x)==1 and y == 0):
        if x % 2 == 1:
          # east/weast
          if ((x+1)//2 + y//2) == 0:
            result += d[(0+rot) % 4]
          else:
            result += d[(2+rot) % 4]
        else:
          # north/south
          if (x//2 + (y+1)//2) == 0:
            result += d[(1+rot) % 4]
          else:
            result += d[(3+rot) % 4]
        x = 0
        y = 0
      else:
        if x % 2 == 1:
          # east/weast
          if ((x+1)//2 + y//2) % 2 == 1:
            result += d[(0+rot) % 4]
            x = (x+1)//2
            y = y//2
          else:
            result += d[(2+rot) % 4]
            x = (x-1)//2
            y = y//2
        else:
          # north/south
          if (x//2 + (y+1)//2) % 2 == 1:
            result += d[(1+rot) % 4]
            x = x//2
            y = (y+1)//2
          else:
            result += d[(3+rot) % 4]
            x = x//2
            y = (y-1)//2

      



  print("Case #%d: %s" % (case, result))