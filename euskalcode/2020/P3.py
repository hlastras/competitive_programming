def find(parent, x):
  if parent[x] != x:
    parent[x] = find(parent, parent[x])
  
  return parent[x]

def union(parent, x, y):
  # print("union",x,y)
  parent[find(parent, x)] = find(parent, y)
  # print(parent)



def strokesRequired(picture):
    
    canvas = []
    for row in picture:
      canvas.append(list(row))

    height = len(canvas)
    width = len(canvas[0])
    subsets = list(range(height * width))
    for row in range(height):
      for col in range(width):
        cell_number = col + (row * width)
        cell_color = canvas[row][col]
        
        # up cell
        if (row - 1) >= 0:
          up_cell_color = canvas[row-1][col]
          if up_cell_color == cell_color:
            up_cell_number = col + ((row - 1) * width)
            union(subsets, up_cell_number, cell_number)
        # # down cell
        # if (row + 1) < height:
        #   down_cell_color = canvas[row+1][col]
        #   if down_cell_color == cell_color:
        #     down_cell_number = col + ((row + 1) * width)
        #     union(subsets, down_cell_number, cell_number)
        # left cell
        if (col - 1) >= 0:
          left_cell_color = canvas[row][col-1]
          if left_cell_color == cell_color:
            left_cell_number = col - 1 + (row * width)
            union(subsets, left_cell_number, cell_number)
        # # right cell
        # if (col + 1) < width:
        #   right_cell_color = canvas[row][col+1]
        #   if right_cell_color == cell_color:
        #     right_cell_number = col + 1 + (row * width)
        #     union(subsets, right_cell_number, cell_number)

    for i in range(len(subsets)):
      # force short path
      find(subsets, i)
    print(subsets)
    return len(set(subsets))


if __name__ == '__main__':
    picture_count = int(input().strip())

    picture = []

    for _ in range(picture_count):
        picture_item = input()
        picture.append(picture_item)

    result = strokesRequired(picture)

    print(result)