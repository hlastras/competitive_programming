import sys
lines = sys.stdin.read().split("\n")

def compare(left, right):
    if type(left) is int and type(right) is int:
        return right - left
        
    elif type(left) is list and type(right) is list:
        for idx in range(min(len(left), len(right))):
            result = compare(left[idx], right[idx])
            if result != 0:
                return result
        if len(left) < len(right):
            return 1
        elif len(left) > len(right):
            return -1
        else:
            return 0

    elif type(left) is list and type(right) is int:
        return compare(left, [right])
    elif type(left) is int and type(right) is list:
        return compare([left], right)

i = 0
total = 0
while i < len(lines):
    left = eval(lines[i])
    right = eval(lines[i+1])

    value = compare(left, right)
    if value > 0:
        total += i//3+1

    i += 3
print(total)