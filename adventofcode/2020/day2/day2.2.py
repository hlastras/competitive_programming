import re
import sys

lines = sys.stdin.read().strip().split("\n")

great = 0
for line in lines:
  match = re.match("(\d+)-(\d+) (\w): (\w+)", line)
  
  position1 = int(match.group(1)) - 1
  position2 = int(match.group(2)) - 1
  character = match.group(3)
  password = match.group(4)
  
  if (password[position1] != password[position2] and 
      (password[position1] == character or password[position2] == character)):
    great += 1

print(great)