import sys
import re
from collections import defaultdict

lines = sys.stdin.read().strip().split("\n")
rules = defaultdict(list)

# We can improve this recursive function to use memoization
def calculate(color):
  total = 1
  for n, c in rules[color]:
    total += (n * calculate(c))
  
  return total

for line in lines:
  outside_color, inside_colors_raw = line.split(" bags contain ", 1)
  for c in inside_colors_raw.split(", "):
    match = re.search(r'(\d)+ ([\w ]+) bag', c)
    if match:
      color = match.group(1)
      rules[outside_color].append((int(match.group(1)), match.group(2)))


total = calculate("shiny gold") - 1 #Subctract 1 because we shouldn't count shiny gold
print(total)

