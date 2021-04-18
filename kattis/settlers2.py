def find_less_used(new_occ):
  # print(new_occ)
  less = 10000000000
  value = 10000000000
  for x in range(1,6):
    if x in new_occ:
      if new_occ[x] < less:
        value = x
        less = new_occ[x]

  return value


board = [1]
occurences = {
  1: 1,
  2: 0,
  3: 0,
  4: 0,
  5: 0
}


count = 1
for i in range(1,59):
  line = 6*i
  before_amount = 6*(i-1)
  off = 0
  first_of_line = count
  for j in range(line):
    # print("CASILLA", count)
    neig = None
    if count%i == 0 and j != line-1:
      off += 1
      neig = [count-1, (count-before_amount-off)]
    elif j == 0:
      neig = [count-1, (count-before_amount-off)]
    elif j == line-1:
      off += 1
      neig = [count-1, (count-before_amount-off), first_of_line]
    else:
      neig = [count-1, (count-before_amount-off), (count-before_amount-off-1)]
    count+=1

    # print(neig)
    
    new_occ = occurences.copy()
    for x in neig:
      if board[x] in new_occ:
        new_occ.pop(board[x])

    less = find_less_used(new_occ)

    board.append(less)
    occurences[less] = occurences[less]+1

    # print(board[-1])


cases = int(input())
for _ in range(cases):
  print(board[int(input())-1])
