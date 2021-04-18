a = input().split(",")
b = input().split(",")

see_a = set()
map_a = {}
see_b = set()
map_b = {}

multi_x = 10000000
x = 0
y = 0

count = 0
for step in a:
  direction = step[0]
  value = int(step[1:])
  for s in range(value):
    count +=1
    if direction == "R":
      y+=1
    elif direction == "L":
      y-=1
    elif direction == "U":
      x+=1
    else:
      x-=1
    point = str(x*multi_x+y)
    see_a.add(point)
    if point not in map_a:
      map_a[point]=count

x = 0
y = 0
count = 0
for step in b:
  direction = step[0]
  value = int(step[1:])
  for s in range(value):
    count +=1
    if direction == "R":
      y+=1
    elif direction == "L":
      y-=1
    elif direction == "U":
      x+=1
    else:
      x-=1
    point = str(x*multi_x+y)
    see_b.add(point)
    if point not in map_b:
      map_b[point]=count

crosses = see_a.intersection(see_b)
min = 10000000
for cross in crosses:
  x = map_a[cross]
  y = map_b[cross]

  if x+y < min:
    min = x+y

print(min)

