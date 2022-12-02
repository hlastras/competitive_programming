instructions = input()

def cord_to_str(x, y):
    return str(x) + ',' + str(y)

visited = {}
x = 0
y = 0
visited[cord_to_str(x, y)] = True
for ch in instructions:
    if ch == '^':
        y += 1
    elif ch == 'v':
        y -= 1
    elif ch == '>':
        x += 1
    else:
        x -= 1
    
    visited[cord_to_str(x, y)] = True

print(len(visited.keys()))
