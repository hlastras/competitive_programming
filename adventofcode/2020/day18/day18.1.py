import sys
lines = sys.stdin.read().strip().split("\n")

def solve(steps):
  total = int(steps.pop(0))
  while len(steps) > 0:
    op = steps.pop(0)
    val = int(steps.pop(0))
    if op == "+":
      total += val
    else:
      total *= val
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