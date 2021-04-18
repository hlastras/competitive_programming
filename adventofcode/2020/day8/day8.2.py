import sys
import re

instructions = sys.stdin.read().strip().split("\n")

acc = 0
pointer = 0

for i in range(len(instructions)):
  if not instructions[i].startswith("acc"):
    # Change instruction
    if instructions[i].startswith("jmp"):
      instructions[i] = instructions[i].replace("jmp", "nop")
    else:
      instructions[i] = instructions[i].replace("nop", "jmp")

    # Execute program
    acc = 0
    pointer = 0
    executed = set()
    fails = False
    while pointer < len(instructions):
      if pointer in executed:
        fails = True
        break
      
      executed.add(pointer)
      match =  match = re.search(r'(\w+) (.{1}\d+)', instructions[pointer])
      type = match.group(1)
      value = int(match.group(2))

      if type == "acc":
        acc += value
        pointer += 1
      elif type == "jmp":
        pointer += value
      elif type == "nop":
        pointer += 1

    # Revert change
    if instructions[i].startswith("jmp"):
      instructions[i] = instructions[i].replace("jmp", "nop")
    else:
      instructions[i] = instructions[i].replace("nop", "jmp")

    if not fails:
      print(acc)
      break
