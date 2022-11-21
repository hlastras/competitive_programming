# Learned how to solve it from here: https://www.ericburden.work/blog/2022/01/05/advent-of-code-2021-day-24/

optype =  [ 1,  1,  1, 26,  1, 26, 26,  1,  26,  1,  1, 26, 26, 26]
correction =  [11, 11, 15,-14, 10,  0, -6, 13,  -3, 13, 15, -2, -9, -2]
offset = [ 6, 14, 13,  1,  6, 13,  6,  3,   8, 14,  4,  7, 15,  1]

result = [0] * 14

stack = []
for i, t in enumerate(optype):
    if t == 1:
        stack.append((i, offset[i]))
    else:
        idx, off = stack[-1]
        stack = stack[:-1]

        diff = off + correction[i]
        a = 1
        b = 1
        if diff < 0:
            a = b - diff
        else:
            b = a + diff
        
        result[idx] = a
        result[i] = b

print(''.join([str(x) for x in result]))