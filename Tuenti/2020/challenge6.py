import socket
from collections import defaultdict

commands = ["2U1R", "1U2R", "1D2R", "2D1R", "2D1L", "1D2L", "1U2L", "2U1L"]
vals = [[-2,1], [-1,2], [1,2], [2,1], [2,-1], [1,-2], [-1,-2], [-2,-1]]
cell_to_command_index = [(1, 7), (3, 0), (5,6), (9, 1), (15, 5), (19, 2), (21, 4), (23, 3)]

def is_visited(visited, point):
  return point[1] in visited[point[0]]

def find_jumps(point, data, visited):
  global vals
  data = data[0:30].replace('\n', '')
  result = []
  for cell, index in cell_to_command_index:
    if data[cell] != "#" and point[1]+vals[index][1] not in visited[point[0]+vals[index][0]]:
      result.append(index)
  return result

def fill_matrix(data, matrix, point):
  data = data[0:30].replace('\n', '')
  x = point[0]
  y = point[1]
  i = 0
  for r in range(x-2,x+3):
    for c in range(y-2,y+3):
      matrix[r][c] = data[i]
      i += 1
  
def print_matrix(matrix):
  for r in matrix:
    l = "".join(r)
    if "#" in l or "." in l:
      print(l)



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("52.49.91.111", 2003))

matrix = []
for _ in range(250):
  matrix.append([" "]*250)

princess_point = [125, 126]
point = [125,125] # Initial knight point
path = []
visited = defaultdict(set)

i = 0
s.recv(1024).decode('ascii')
while True:
  if i >= 0:
    s.sendall(commands[i].encode())
    data = s.recv(1024).decode('ascii')
    path.append([point, commands[(i+4)%8]])
    point = [point[0]+vals[i][0], point[1]+vals[i][1]]
    visited[point[0]].add(point[1])
  else:
    # Back
    b = path.pop()
    point = b[0]
    comm = b[1]
    s.sendall(comm.encode())
    data = s.recv(1024).decode('ascii')

  if point[0] == princess_point[0] and point[1] == princess_point[1]:
    print(data)
    exit(0)
  
  fill_matrix(data, matrix, point)
  print_matrix(matrix)

  available_jumps = find_jumps(point, data, visited)
  if len(available_jumps) > 0:
    i = available_jumps[0]
  else:
    i = -1
