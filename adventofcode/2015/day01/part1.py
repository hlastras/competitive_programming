instructions = input()

count = 0
for c in instructions:
    if c == '(':
        count += 1
    else:
        count -= 1

print(count)