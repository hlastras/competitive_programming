import sys
lines = sys.stdin.read().split("\n")

vowels = ['a', 'e', 'i', 'o', 'u']
not_allowed = ['ab', 'cd', 'pq', 'xy']
total = 0
for line in lines:
    vowels_count = 0
    for ch in line:
        if ch in vowels:
            vowels_count += 1
    if vowels_count < 3:
        continue

    repeated = False
    for idx, ch in enumerate(line[:-1]):
        if ch == line[idx+1]:
            repeated = True
            break
    if not repeated:
        continue

    any_not_allowed = False
    for a in not_allowed:
        if a in line:
            any_not_allowed = True
    if any_not_allowed:
        continue

    total += 1
print(total)