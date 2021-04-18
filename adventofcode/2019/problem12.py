class Moon():
  def __init__(self, line):
    x, y, z = self.parse(line)
    self.pos_x = x
    self.pos_y = y
    self.pos_z = z

    self.vel_x = 0
    self.vel_y = 0
    self.vel_z = 0

  def parse(self, line):
    i = line.index("=")+1
    e = line.index(",")
    x = line[i:e]
    
    i = line.index("=", e+1)+1
    e = line.index(",", e+1)
    y = line[i:e]

    i = line.index("=", e+1)+1
    e = line.index(">", e+1)
    z = line[i:e]

    return int(x), int(y), int(z)

  def gravity(self, other_moon):
    if self.pos_x < other_moon.pos_x:
      self.vel_x += 1
    elif self.pos_x > other_moon.pos_x:
      self.vel_x -= 1

    if self.pos_y < other_moon.pos_y:
      self.vel_y += 1
    elif self.pos_y > other_moon.pos_y:
      self.vel_y -= 1

    if self.pos_z < other_moon.pos_z:
      self.vel_z += 1
    elif self.pos_z > other_moon.pos_z:
      self.vel_z -= 1

  def velocity(self):
    self.pos_x += self.vel_x
    self.pos_y += self.vel_y
    self.pos_z += self.vel_z

  def energy(self):
    a = (abs(self.pos_x) + abs(self.pos_y) + abs(self.pos_z))
    b = (abs(self.vel_x) + abs(self.vel_y) + abs(self.vel_z))
    # if b==0:
    #   print(a,b)
    return a * b, b

  def print(self):
    print("pos=<x=%d, y=%d, z=%d>, vel=<x=%d, y=%d, z=%d>" % (self.pos_x, self.pos_y, self.pos_z, self.vel_x, self.vel_y, self.vel_z))


import sys
lines = sys.stdin.read().split("\n")
moons = []
for line in lines:
  moons.append(Moon(line))

# for m in moons:
#   m.print()

for step in range(1, 275075888):
  # print("STEP:", step)

  for i, moon1 in enumerate(moons[:-1]):
    for moon2 in moons[i+1:]:
      moon1.gravity(moon2)
      moon2.gravity(moon1)
  
  for m in moons:
    m.velocity()

  total_energy = 0
  for m in moons:
    total_energy += m.energy()[1]
  if total_energy == 0:
    print(total_energy,step)

  # for m in moons:
  #   m.print()

  # print()
  # print()

total_energy = 0
for m in moons:
  total_energy += m.energy()[0]
print(total_energy)
