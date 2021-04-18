import sys

instructions = sys.stdin.read().strip().split("\n")

x = 0
y = 0
direction = 90

for inst in instructions:
  action = inst[0]
  value = int(inst[1:])

  if action == "F":
    if direction == 0:
      action = "N"
    elif direction == 90:
      action = "E"
    elif direction == 180:
      action = "S"
    elif direction == 270:
      action = "W"


  if action == "N":
    y += value
  elif action == "S":
    y -= value
  elif action == "E":
    x += value
  elif action == "W":
    x -= value
  elif action == "L":
    direction = (direction - value) % 360
  elif action == "R":
    direction = (direction + value) % 360

print(abs(x) + abs(y))

