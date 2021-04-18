import sys

instructions = sys.stdin.read().strip().split("\n")

x = 0
y = 0
waypoint_x = 10
waypoint_y = 1

for inst in instructions:
  action = inst[0]
  value = int(inst[1:])

  if action == "F":
    x += (value * waypoint_x)
    y += (value * waypoint_y)
  elif action == "N":
    waypoint_y += value
  elif action == "S":
    waypoint_y -= value
  elif action == "E":
    waypoint_x += value
  elif action == "W":
    waypoint_x -= value
  elif action == "L":
    for _ in range(value//90):
      tmp = waypoint_x
      waypoint_x = -waypoint_y
      waypoint_y = tmp
  elif action == "R":
    for _ in range(value//90):
      tmp = waypoint_y
      waypoint_y = -waypoint_x
      waypoint_x = tmp

print(abs(x) + abs(y))

