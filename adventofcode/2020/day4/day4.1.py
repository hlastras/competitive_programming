import sys

lines = sys.stdin.read().strip().split("\n\n")

required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

total = 0
for line in lines:
  valid = True
  for rf in required_fields:
    if rf not in line:
      valid = False
      break

  if valid:
    total += 1

print(total)