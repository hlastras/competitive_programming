import sys
lines = sys.stdin.read().split("\n")[:-1]

inp = [1,1,1,1,1,1,1,1,1,1,1,1,1,1]

count = 0
registers = [0, 0, 0, 0]
reg_name_idx = {'x': 0, 'y': 1, 'z': 2, 'w': 3}

def read_value(x):
    if x in reg_name_idx.keys():
        return registers[reg_name_idx[x]]
    else:
        return int(x)

for line in lines:
    instruction = line.split()
    
    op = instruction[0]
    if op == 'inp':
        value = inp[count]
        count += 1
        registers[reg_name_idx[instruction[1]]] = value

    if op == 'add':
        value = read_value(instruction[2])
        registers[reg_name_idx[instruction[1]]] += value

    if op == 'mul':
        value = read_value(instruction[2])
        registers[reg_name_idx[instruction[1]]] *= value

    if op == 'div':
        value = read_value(instruction[2])
        registers[reg_name_idx[instruction[1]]] = registers[reg_name_idx[instruction[1]]] // value

    if op == 'mod':
        value = read_value(instruction[2])
        registers[reg_name_idx[instruction[1]]] = registers[reg_name_idx[instruction[1]]] % value

    if op == 'eql':
        value1 = registers[reg_name_idx[instruction[1]]]
        value2 = read_value(instruction[2])
        if value1 == value2:
            registers[reg_name_idx[instruction[1]]] = 1
        else:
            registers[reg_name_idx[instruction[1]]] = 0

print(registers[2])