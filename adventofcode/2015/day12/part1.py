import re
json = input()

r = sum([int(x) for x in re.findall(r"-?\d+", json)])
print(r)

