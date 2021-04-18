import sys
lines = sys.stdin.read().strip().split("\n")

def solve(steps):
  steps2 = []
  steps2.append(int(steps.pop(0)))
  while len(steps) > 0:
    op = steps.pop(0)
    if op == "+":
      a = steps2.pop()
      b = steps.pop(0)
      steps2.append(int(a) + int(b))
    else:
      steps2.append(int(steps.pop(0)))

  total = 1
  for i in steps2:
    total *= i
  return total

total = 0
for operation in lines:
  operation = operation.replace("(", "( ").replace(")", " )").split(" ")

  stack = []
  for i in operation:
    if i == ")":
      par = []
      n = stack.pop()
      while n != "(":
        par.append(n)
        n = stack.pop()
      par.reverse()
      stack.append(solve(par))
    else:
      stack.append(i)

  total += solve(stack)

print(total)