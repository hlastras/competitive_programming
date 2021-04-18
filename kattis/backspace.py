from collections import deque
line = input()

stack = deque()

for c in line:
  if c != '<':
    stack.append(c)
  elif len(stack) > 0:
      stack.pop()

print("".join(stack))
