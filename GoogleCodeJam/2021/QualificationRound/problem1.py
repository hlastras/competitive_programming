cases = int(input())
for c in range(1, cases+1):
  input() # Discard lenght
  numbers = list(map(int, input().split()))

  sol = 0
  for i in range(len(numbers)-1):

    index = numbers.index(min(numbers[i:])) + 1
    sol += (index - i)
    numbers[i:index] = numbers[i:index][::-1]

  print(f'Case #{str(c)}: {str(sol)}')
