import sys
import math
lines = sys.stdin.read().split("\n")
phases = max(len(lines), len(lines[0]))
asteroid_map = list("".join(lines))

width = len(lines[0])
numbers = []
for phase in range(1,phases):
  numbers.append(phase)
  numbers.append(-phase)
  numbers.append(phase*width)
  numbers.append(-phase*width)
  numbers.append(phase+phase*width)
  numbers.append(phase-phase*width)
  numbers.append(-phase+phase*width)
  numbers.append(-phase-phase*width)
  for micro_phase in range(1, phase):
    numbers.append(phase+micro_phase*width)
    numbers.append(phase-micro_phase*width)
    numbers.append(-phase+micro_phase*width)
    numbers.append(-phase-micro_phase*width)
    numbers.append(micro_phase+phase*width)
    numbers.append(micro_phase-phase*width)
    numbers.append(-micro_phase+phase*width)
    numbers.append(-micro_phase-phase*width)
    
for i, x in enumerate(asteroid_map):
  if x=="#":
    new_asteroid_map = asteroid_map.copy()

    
