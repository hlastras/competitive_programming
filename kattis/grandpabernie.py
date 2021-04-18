a = int(input())

s = {}

for _ in range(a):
  country, year = input().split()
  if country not in s:
    s[country] = []

  s[country].append(int(year))

for key in s.keys():
  s[key].sort()


b = int(input())
responses = []
for _ in range(b):
  country, order = input().split()
  responses.append(str(s[country][int(order)-1]))

print("\n".join(responses))