import re

z = input()
z = re.sub(r"[a-z]", " ", z)
z = re.sub(r" +", " ", z)

print(len(set(map(int, z.strip().split(" ")))))