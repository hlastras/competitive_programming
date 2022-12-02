instructions = input()

count = 0
for idx, char in enumerate(instructions):
    if char == '(':
        count += 1
    else:
        count -= 1

    if count < 0:
        print(idx + 1)
        break