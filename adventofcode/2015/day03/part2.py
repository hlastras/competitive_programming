instructions = input()

def cord_to_str(x, y):
    return str(x) + ',' + str(y)

visited = {}
x = [0,0]
y = [0,0]
visited[cord_to_str(x[0], x[1])] = True
for ch in instructions:
    if ch == '^':
        x[1] += 1
    elif ch == 'v':
        x[1] -= 1
    elif ch == '>':
        x[0] += 1
    else:
        x[0] -= 1
    
    visited[cord_to_str(x[0], x[1])] = True
    x, y = y, x

print(len(visited.keys()))