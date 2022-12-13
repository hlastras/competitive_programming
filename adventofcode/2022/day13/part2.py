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

def bubbleSort(arr):
    swapped = False
    for i in range(len(arr)-1):
        for j in range(0, len(arr)-i-1):
            if compare(arr[j], arr[j + 1]) < 0:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
            return

packets = [[[2]], [[6]]]
for line in lines:
    if line == '':
        continue
    packets.append(eval(line))

bubbleSort(packets)

print((packets.index([[2]])+1) * (packets.index([[6]])+1))