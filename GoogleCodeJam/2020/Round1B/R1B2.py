


f = open("out.txt", "w")
def my_input():
  r = input()
  global f
  f.write("< ")
  f.write(r)
  f.write("\n")
  return r

def my_print(output):
  global f
  print(output)
  f.write(">>> ")
  f.write(str(output))
  f.write("\n")

points = [[0,0], 
  [500000000, 500000000], 
  [-500000000, 500000000], 
  [500000000, -500000000], 
  [-500000000, -500000000],
  [750000000, 750000000],
  [250000000, 750000000],
  [750000000, 250000000],
  [250000000, 250000000],
  [-750000000, 750000000],
  [-250000000, 750000000],
  [-750000000, 250000000],
  [-250000000, 250000000],
  [-750000000, -750000000],
  [-250000000, -750000000],
  [-750000000, -250000000],
  [-250000000, -250000000],
  [750000000, -750000000],
  [250000000, -750000000],
  [750000000, -250000000],
  [250000000, -250000000],
  ]

t, a, b = map(int, my_input().split())

for _ in range(t):
  finding_point = True
  pos = -1
  hit_point = None
  result = ""
  p = []
  search = None
  while True:
    if finding_point:
      pos += 1
      my_print("%d %d" % (points[pos][0], points[pos][1]))
      result = my_input()
      if result == "HIT":
        finding_point = False
        hit_point = points[pos]
    else:
      if len(p) == 0:
        if search == None:
          search = [-1000000000, hit_point[0]]
        x = (search[0] + search[1]) // 2
        my_print("%d %d" % (x, hit_point[1]))
        result = my_input()
        if result == "HIT":
          search[1]=x
        elif result == "MISS":
          search[0]=x+1
        if search[0] >= search[1]:
          p.append(search[0])
          search = None

      elif len(p) == 1:
        if search == None:
          search = [hit_point[0], 1000000000]
        x = (search[0] + search[1]) // 2
        my_print("%d %d" % (x, hit_point[1]))
        result = my_input()
        if result == "HIT":
          search[0]=x+1
        elif result == "MISS":
          search[1]=x
        if search[0]+1 >= search[1]:
          p.append(search[0])
          search = None

      elif len(p) == 2:
        if search == None:
          search = [-1000000000, hit_point[1]]
        y = (search[0] + search[1]) // 2
        my_print("%d %d" % (hit_point[0], y))
        result = my_input()
        if result == "HIT":
          search[1]=y
        elif result == "MISS":
          search[0]=y+1
        if search[0] >= search[1]:
          p.append(search[0])
          search = None




        f.write("---------------- ")
        f.write(str("%d %d" % (search[0], search[1])))
        f.write("\n")
      elif len(p) == 3:
        if search == None:
          search = [hit_point[1], 1000000000]
        y = (search[0] + search[1]) // 2
        my_print("%d %d" % (hit_point[0], y))
        result = my_input()
        if result == "HIT":
          search[1]=y
        elif result == "MISS":
          search[0]=y+1
        if search[0] >= search[1]:
          p.append(search[0])
          search = None

    if result == "CENTER":
      break



  
  



f.close()