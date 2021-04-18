import math
def valid_position(x,y,w,h,hidden):
  return x>=0 and x<w and y>=0 and y<h and (y*w+x) not in hidden
def angle(col,row,x,y):
  return (x-col) / math.sqrt((x-col)**2+(y-row)**2)

def add_hidden(hidden, col, row, x, y, w, h):
  # print("ADDING_H", x,y)
  # print(x-col, y-row)
  an = angle(col, row, x, y)
  # print("angle",an)

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

  # print("Zzzzzz")
  for s in range_y:
    for ss in range_x:
      # print("sssssss",col,row,ss,s, an, angle(col,row,ss,s))
      
      if math.isclose(an,angle(col,row,ss,s)):
        hidden.add(s*w+ss)


import sys
import math
lines = sys.stdin.read().split("\n")
phases = max(len(lines), len(lines[0]))
asteroid_map = list("".join(lines))

w = len(lines[0])
h = len(lines)

maxim = 0
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
      maxim = max(seen, maxim)

print(maxim)

    
