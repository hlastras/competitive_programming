import sys
lines = sys.stdin.read().split("\n")

vowels = ['a', 'e', 'i', 'o', 'u']
not_allowed = ['ab', 'cd', 'pq', 'xy']
total = 0
for line in lines:
    
    valid = False
    for i in range(len(line)-2):
        x = line[i:i+2]
        for j in range(i+2, len(line)-1):
            if x == line[j:j+2]:
                valid = True
                break

    if not valid:
        continue

    valid = False
    for i in range(len(line)-2):
        if line[i] == line[i+2] and line[i] != line[i+1]:
            valid = True

    if not valid:
        continue


    total += 1
print(total)