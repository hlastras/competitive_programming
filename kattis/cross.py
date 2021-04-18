def print_matrix(matrix):
  for r in matrix:
    print("".join(r))

def is_valid(matrix):
  for number in range(1,10):

    for r in matrix:
      count = 0
      for x in r:
        if x == str(number):
          count += 1
      if count > 1:
        return False 

    for c in range(9):
      count = 0
      for r in range(9):
        if matrix[r][c] == str(number):
          count += 1
      if count > 1:
        return False

    for r in range(0, 9, 3):
      for c in range(0, 9, 3):
        count = 0
        for x in range(r, r+3):
          for y in range(c, c+3):
            if matrix[x][y] == str(number):
              count += 1
        if count > 1:
          return False

  return True


def fit_in_cell(col, row, number, matrix):
  if matrix[row][col] != ".":
    return False
  
  for r in range(9):
    if matrix[r][col] == str(number):
      return False

  for c in range(9):
    if matrix[row][c] == str(number):
      return False

  return True

def fits_in_square(col, row, number, matrix):
  fetch_in_square = []
  for c in range(col, col+3):
    for r in range(row, row+3):
      if matrix[r][c] == str(number):
        return []

      if fit_in_cell(c, r, number, matrix):
        fetch_in_square.append([r, c])

  if len(fetch_in_square) == 0:
    return False
  return fetch_in_square

def repeated_points(to_add):
  aux = []
  for x in to_add:
    aux.append(x[0])

  for i in range(len(aux)):
    for j in range(i+1, len(aux)):
      if aux[i] == aux[j]:
        return True
  
  return False

matrix = []
matrix_original = []

for _ in range(9):
  row = list(input())
  matrix.append(row)
  matrix_original.append(row.copy())

if is_valid(matrix):
  added = 1
  while added != 0:
    added = 0
    to_add = []
    for number in range(1, 10):
      fetch_in_square = 0
      for square_c in range(0, 9, 3):
        for square_r in range(0, 9, 3):
          fits = fits_in_square(square_c, square_r, number, matrix)
          if fits == False:
            print("ERROR")
            exit(0)
          if len(fits) == 1:
            to_add.append([fits[0], number])
            added += 1
    if repeated_points(to_add):
      matrix = matrix_original
      break
    for [r, c], number in to_add:
      matrix[r][c] = str(number)


  print_matrix(matrix)
else:
  print("ERROR")

