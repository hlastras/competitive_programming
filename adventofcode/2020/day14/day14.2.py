import sys
import re
from collections import Counter
from copy import deepcopy
mem_instruction = r'mem\[(\d+)\] = (\d+)'
instructions = sys.stdin.read().strip().split("\n")

mask = None
mask_floating_count = 0
mem = {}
for line in instructions:
  if line.startswith("mask"):
    mask = line[7:]
    mask_floating_count = Counter(mask)["X"]
  else:
    match =  match = re.search(mem_instruction, line)
    mem_pos = int(match.group(1))
    value = int(match.group(2))
    
    binary = list(format(mem_pos, '#038b')[2:])
    for i, v in enumerate(mask):
      if v != "0":
        binary[i] = v

    pattern = deepcopy(binary)

    for i in range(2**mask_floating_count):
      b = list(format(i, '#0'+str(mask_floating_count+2)+'b')[2:])
      c = 0
      for j, char in enumerate(pattern):
        if char == "X":
          binary[j] = b[c]
          c += 1

      m = int("".join(binary), 2)
      mem[m] = value


total = sum(mem.values())
print(total)