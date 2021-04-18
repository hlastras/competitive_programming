import sys
import re
mem_instruction = r'mem\[(\d+)\] = (\d+)'
instructions = sys.stdin.read().strip().split("\n")

mask = None
mem = {}
for line in instructions:
  if line.startswith("mask"):
    mask = line[7:]
  else:
    match =  match = re.search(mem_instruction, line)
    mem_pos = int(match.group(1))
    value = int(match.group(2))
    
    binary = list(format(value, '#038b')[2:])
    for i, v in enumerate(mask):
      if v != "X":
        binary[i] = v
    binary = "".join(binary)

    value = int(binary, 2)
    mem[mem_pos] = value

total = sum(mem.values())
print(total)