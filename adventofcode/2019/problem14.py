import sys
import math
lines = sys.stdin.read().split("\n")

reactions = {}

for l in lines:
  inputs, outputs = l.split(" => ")
  value, quim = outputs.split(" ")
  ins = []
  for i in inputs.split(", "):
    v, q = i.split(" ")
    ins.append((int(v), q))
  reactions[quim] = (int(value), ins)

rests = {}
raw = 0
level = reactions["FUEL"][1]
while len(level)>0:
  new_level = []

  for v, q in level:
    if q == "ORE":
      raw += v
    else:
      if q in rests:
        m = min(rests[q], v)
        v -= m
        rests[q] -= m
      
      if v > 0:
        crea, neces = reactions[q]
        n = int(math.ceil(v/crea))
        rest = crea*n - v
        if q not in rests:
          rests[q] = 0
        rests[q] += rest
        for a, b in neces:
          new_level.append((a*n, b))
  level = new_level
print(raw)


