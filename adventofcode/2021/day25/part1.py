import sys
lines = sys.stdin.read().split("\n")[:-1]

data = []
for l in lines:
    data.append([x for x in l])

height = len(data)
width = len(data[0])
any_move = True
count = 0
while any_move:
    any_move = False

    for l in data:
        tmp = l[0]
        idx = 0 
        while idx < width-1:
            if l[idx] == '>' and l[(idx+1) % width] == '.':
                l[idx] = '.' 
                l[(idx+1) % width] = '>'
                idx += 1
                any_move = True
            
            idx += 1

        if idx == width-1 and l[-1] == '>' and tmp == '.':
            l[-1] = '.' 
            l[0] = '>'
            any_move = True

    for col in range(width):
        tmp = data[0][col]
        idx = 0 
        while idx < height-1:
            if data[idx][col] == 'v' and data[(idx+1) % height][col] == '.':
                data[idx][col] = '.' 
                data[(idx+1) % height][col] = 'v'
                idx += 1
                any_move = True
            
            idx += 1
        
        if idx == height-1 and data[-1][col] == 'v' and tmp == '.':
            data[-1][col] = '.' 
            data[0][col] = 'v'
            any_move = True
    
    count += 1

print(count)