import sys
import math

def valid_position(x,y,w,h,hidden):
  return x>=0 and x<w and y>=0 and y<h and (y*w+x) not in hidden

def angle(col,row,x,y):
  return (x-col) / math.sqrt((x-col)**2+(y-row)**2)
def angle2(col,row,x,y):
  deg =  math.degrees(math.asin( (x-col) / math.sqrt((x-col)**2+(y-row)**2) ))
  # print(col,row,x,y,(x-col),(y-row),deg)

  if deg>=0:
    if (y-row)>0:
      deg = 180-deg
  else:
    if (y-row)>0:
      deg = 180-deg
    else:
      deg = 360+deg

  # if (x-col)<0 and (y-row)<=0:
  #   deg = 360+deg
  # elif (x-col)>=0 and (y-row)<0:
  #   deg = deg
  # elif (x-col)>0 and (y-row)>0:
  #   deg=deg+90
  # elif (x-col)<=0 and (y-row)>0:
  #   deg=180+deg

  # print(col,row,x,y,(x-col),(y-row),deg)
  deg = (deg*100000) // 1
  if (str(deg)[-6:] == "9999.0"):
    deg += 1
  return deg


def add_hidden(hidden, col, row, x, y, w, h):
  an = angle(col, row, x, y)

  range_x = None
  if x-col > 0:
    range_x = range(x+1,w,1)
  elif x-col < 0:
    range_x = range(x-1,-1,-1)
  else:
    range_x = range(x,x+1)

  range_y = None
  if y-row > 0:
    range_y = range(y+1,h,1)
  elif y-row < 0:
    range_y = range(y-1,-1,-1)
  else:
    range_y = range(y,y+1)

  for s in range_y:
    for ss in range_x:
      if math.isclose(an,angle(col,row,ss,s)):
        hidden.add(s*w+ss)



lines = sys.stdin.read().split("\n")
phases = max(len(lines), len(lines[0]))
asteroid_map = list("".join(lines))

w = len(lines[0])
h = len(lines)

maxim = 0
maxim_x = -1
maxim_y = -1
for row in range(len(lines)):
  for col in range(len(lines[0])):
    if asteroid_map[row*w+col] == "#":
      # print("EMPEZAMOS",col,row)
      seen = 0
      hidden = set()
      for i in range(1,w+1):
        y = row - i
        x = col - i
        for _ in range(2*i):
          if valid_position(x,y,w,h,hidden) and asteroid_map[y*w+x] == "#" :
            seen += 1
            add_hidden(hidden, col, row, x, y, w, h)
          # print(x,y)
          x+=1
        for _ in range(2*i):
          if valid_position(x,y,w,h,hidden) and asteroid_map[y*w+x] == "#":
            seen += 1
            add_hidden(hidden, col, row, x, y, w, h)
          # print(x,y)
          y+=1
        for _ in range(2*i):
          if valid_position(x,y,w,h,hidden) and asteroid_map[y*w+x] == "#":
            seen += 1
            add_hidden(hidden, col, row, x, y, w, h)
          # print(x,y)
          x-=1
        for _ in range(2*i):
          if valid_position(x,y,w,h,hidden) and asteroid_map[y*w+x] == "#":
            seen += 1
            add_hidden(hidden, col, row, x, y, w, h)
          # print(x,y)
          y-=1
      # print(col,row,seen)
      if seen > maxim:
        maxim = seen
        maxim_y = row
        maxim_x = col

      maxim = max(seen, maxim)

print(maxim_x, maxim_y)



row = maxim_y
col = maxim_x
hidden = set()
seen = {}

for i in range(1,w+1):
  y = row - i
  x = col - i
  for _ in range(2*i):
    if valid_position(x,y,w,h,hidden) and asteroid_map[y*w+x] == "#" :
      a = angle2(col, row, x, y)
      if a not in seen:
        seen[a] = []
      seen[a].append((x,y))
    # print(x,y)
    x+=1
  for _ in range(2*i):
    if valid_position(x,y,w,h,hidden) and asteroid_map[y*w+x] == "#":
      a = angle2(col, row, x, y)
      if a not in seen:
        seen[a] = []
      seen[a].append((x,y))
    # print(x,y)
    y+=1
  for _ in range(2*i):
    if valid_position(x,y,w,h,hidden) and asteroid_map[y*w+x] == "#":
      a = angle2(col, row, x, y)
      if a not in seen:
        seen[a] = []
      seen[a].append((x,y))
    # print(x,y)
    x-=1
  for _ in range(2*i):
    if valid_position(x,y,w,h,hidden) and asteroid_map[y*w+x] == "#":
      a = angle2(col, row, x, y)
      if a not in seen:
        seen[a] = []
      seen[a].append((x,y))
    # print(x,y)
    y-=1

values = list(seen.keys()).copy()
values.sort()
print(seen)
count = 0
while count<200:
  for x in values:
    z = seen[x]
    if len(z) > 0:
      a = z[0]
      seen[x] = z[1:]
      count += 1
      print(count, a, x)
      if count == 200:
        print(a[0]*100+a[1])
        break



    
