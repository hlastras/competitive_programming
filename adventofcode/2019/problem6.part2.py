import sys
lines = sys.stdin.read().split("\n")
graph = {}
for line in lines:
  a, b = line.split(")")
  graph[b] = a

actual = "YOU"
path_you = []
while actual != 'COM':
  actual = graph[actual]
  path_you.append(actual)

actual = "SAN"
path_san = []
while actual != 'COM':
  actual = graph[actual]
  path_san.append(actual)

path_you.reverse()
path_san.reverse()
count = 0
while path_you[count] == path_san[count]:
  count += 1



print( len(path_you[count:]) + len(path_san[count:]) )


