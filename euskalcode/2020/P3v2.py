def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    parent[find(parent, x)] = find(parent, y)



def strokesRequired(picture):
    canvas = []
    for row in picture:
      canvas.append(list(row))

    height = len(canvas)
    width = len(canvas[0])
    print(height * width)
    subsets = list(range(height * width))
    for row in range(height):
      for col in range(width):
        cell_number = col + (row * width)
        cell_color = canvas[row][col]
        
        # up cell
        if (row - 1) >= 0 and cell_color == canvas[row-1][col]:
          up_cell_number = col + ((row - 1) * width)
          union(subsets, cell_number, up_cell_number, )
        
        # left cell
        if (col - 1) >= 0 and cell_color == canvas[row][col-1]:
          left_cell_number = col - 1 + (row * width)
          union(subsets, cell_number, left_cell_number,)

    for i in range(len(subsets)):
      # force short path
      find(subsets, i)

    return len(set(subsets))


if __name__ == '__main__':
    picture_count = int(input().strip())

    picture = []

    for _ in range(picture_count):
        picture_item = input()
        picture.append(picture_item)

    result = strokesRequired(picture)

    print(result)