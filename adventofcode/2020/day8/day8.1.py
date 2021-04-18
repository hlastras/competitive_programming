import sys
import re

instructions = sys.stdin.read().strip().split("\n")

acc = 0
pointer = 0
executed = set()
while True:
  if pointer in executed:
    print(acc)
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
