t = int(input())

for _ in range(t):
  row, col = [int(x) for x in input().split()]
  layer = max(row,col)
  initial_value = ((layer-1)**2)+1
  if layer % 2 == 1:
    row, col = col, row
  
  increment = (row-1)
  if row == layer:
    increment += (layer-col)

  print(initial_value+increment)
