a = input().split(",")
b = input().split(",")

see_a = set()
see_b = set()

multi_x = 100000
x = 0
y = 0

for step in a:
  direction = step[0]
  value = int(step[1:])
  for s in range(value):
    if direction == "R":
      y+=1
    elif direction == "L":
      y-=1
    elif direction == "U":
      x+=1
    else:
      x-=1
    see_a.add(x*multi_x+y)


x = 0
y = 0
for step in b:
  direction = step[0]
  value = int(step[1:])
  for s in range(value):
    if direction == "R":
      y+=1
    elif direction == "L":
      y-=1
    elif direction == "U":
      x+=1
    else:
      x-=1
    see_b.add(x*multi_x+y)

crosses = see_a.intersection(see_b)
min = 100000
for cross in crosses:
  x = cross // multi_x
  y = cross % multi_x
  dist = abs(x)+abs(y)
  if dist < min:
    min = dist

print(min)

