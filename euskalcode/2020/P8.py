better = 0
def generate(m, sp, rel, max, pos):
  print(pos)
  if len(rel) >= max or pos >= len(m):
    return 

  # Add
  s, r = m[pos]
  a = sp + s
  rel.append(r)
  b = min(rel)
  global better
  if a * b > better:
    better = a*b
    print(better)
  generate(m, a, rel, max, pos+1)

  rel.pop()

  # Not add
  generate(m, sp, rel, max, pos+1)




def maximumClusterQuality(speed, reliability, maxMachines):
    print(speed, reliability, maxMachines)
    m = []
    for i in range(len(speed)):
      m.append([speed[i], reliability[i]])

    generate(m, 0, [], maxMachines, 0)
    global better
    return better

if __name__ == '__main__':
    speed_count = int(input().strip())

    speed = []

    for _ in range(speed_count):
        speed_item = int(input().strip())
        speed.append(speed_item)

    reliability_count = int(input().strip())

    reliability = []

    for _ in range(reliability_count):
        reliability_item = int(input().strip())
        reliability.append(reliability_item)

    maxMachines = int(input().strip())

    print(maximumClusterQuality(speed, reliability, maxMachines))

