import sys
lines = sys.stdin.read().split("\n")

calories_by_elf = []
current = 0
for line in lines:
    if line == "":
        calories_by_elf.append(current)
        current = 0
    else:
        current += int(line)
if current != 0:
   calories_by_elf.append(current) 

calories_by_elf.sort(reverse=True)

print(sum(calories_by_elf[:3]))