import math
import sys
lines = sys.stdin.read().split("\n")

def decode_digit(digit):
    if digit == "-":
        return -1
    elif digit == "=":
        return -2
    return int(digit)

def encode_digit(digit):
    if digit == -1:
        return '-'
    elif digit == -2:
        return '='
    return str(digit)

def decode_number(line):
    number = 0
    idx = 1
    for d in line[::-1]:
        number += idx * decode_digit(d)
        idx *= 5
    return number

total = 0
for line in lines:
    total += decode_number(line)

print(total)

# TODO improve this shit
digits = []
for x in range(int(math.log10(total)/math.log10(5))+1, -1, -1):
    base = 5**x
    best_idx = 0
    best = abs(total) * 10000
    for y in range(2,-3,-1):
        new_value = total - base*y
        a1 = abs(2*(base//5)-new_value)
        a2 = abs(-2*(base//5)-new_value)
        be = min(a1, a2)
        if be < best:
            best = be
            best_idx = y
    
    total -= base*best_idx
    digits.append(best_idx)

if digits[0] == 0:
    digits = digits[1:]

print(''.join([encode_digit(x) for x in digits]))

