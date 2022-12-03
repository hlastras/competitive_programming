import sys
lines = sys.stdin.read().split("\n")

total = 0
for line in lines:
    first = set(line[:len(line)//2])
    second = set(line[len(line)//2:])

    shared = first & second

    for s in shared:
        v = ord(s)
        if v < 91:
            # is uppercase
            v -= 38
        else:
            # is downcase
            v -= 96

        total += v

print(total)